import os
import shutil
from pathlib import Path

import pytest
from nmk.tests.tester import NmkBaseTester


class TestProtoPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def target_proto_folder(self, module_name: str = None) -> Path:
        return self.test_folder / "protos" / ((Path("sample_module") / "api") if module_name is None else module_name)

    def target_proto(self, module_name: str = None) -> Path:
        return self.target_proto_folder(module_name) / "sample.proto"

    def target_proto2(self, module_name: str = None) -> Path:
        return self.target_proto_folder(module_name) / "sample2.proto"

    def prepare_proto_project(self, other_plugin: str = None, extra_proto: Path = None, module_name: str = None) -> Path:
        # Build a sample project with proto files
        self.target_proto_folder(module_name).mkdir(exist_ok=True, parents=True)
        shutil.copyfile(self.template(self.target_proto(module_name).name), self.target_proto(module_name))
        if extra_proto is not None:
            shutil.copyfile(self.template(extra_proto.name), extra_proto)
        return self.prepare_project(f"ref_proto{('_' + other_plugin) if other_plugin is not None else ''}.yml")

    def escape(self, to_escape: Path) -> str:
        # Escape backslashes (for Windows paths in json print)
        return '"' + str(to_escape).replace("\\", "\\\\") + '"'

    def test_version(self):
        self.nmk(self.prepare_proto_project(), extra_args=["version"])

    def test_proto_files(self):
        # Check found proto files
        self.nmk(self.prepare_proto_project(), extra_args=["--print", "protoInputFiles", "--print", "protoAllInputSubDirs"])
        self.check_logs(
            f'{{ "protoInputFiles": [ {self.escape(self.target_proto())} ], "protoAllInputSubDirs": [ {self.escape(Path("sample_module") / "api")} ] }}'
        )

    def test_vscode_settings(self):
        # Verify generated settings
        self.nmk(self.prepare_proto_project("vscode"), extra_args=["vs.settings"])
        settings = self.test_folder / ".vscode" / "settings.json"
        assert settings.is_file()

    def test_python_files_without_python(self):
        # Verify that there are no expected python files without python plugin
        self.nmk(
            self.prepare_proto_project(),
            extra_args=["--print", "pythonGeneratedSrcFiles", "--print", "protoPythonCopiedFiles", "--print", "protoPythonSrcFolders"],
        )
        self.check_logs('{ "pythonGeneratedSrcFiles": [], "protoPythonCopiedFiles": [], "protoPythonSrcFolders": [] }')

    def test_python_files(self):
        # Verify expected python files
        self.nmk(
            self.prepare_proto_project("python"),
            extra_args=["--print", "pythonGeneratedSrcFiles", "--print", "protoPythonCopiedFiles", "--print", "protoPythonSrcFolders"],
        )
        src_path = self.test_folder / "src" / "sample_module" / "api"
        self.check_logs(
            f'{{ "pythonGeneratedSrcFiles": [ {self.escape(src_path / "sample_pb2.py")}, {self.escape(src_path / "sample_pb2_grpc.py")}, {self.escape(src_path.parent / "__init__.py")}, {self.escape(src_path / "__init__.py")} ], '
            + f'"protoPythonCopiedFiles": [ {self.escape(src_path / "sample.proto")} ], '
            + f'"protoPythonSrcFolders": [ {self.escape(src_path.parent)}, {self.escape(src_path)} ] }}'
        )

    def test_generate_python(self):
        # Generate python code from proto (declared as dependency of python code format)
        project = self.prepare_proto_project("python")
        self.nmk(project, extra_args=["git.ignore", "py.format"])
        src_path = self.test_folder / "src" / "sample_module" / "api"
        assert (src_path / "sample_pb2.py").is_file()
        assert (src_path / "sample_pb2_grpc.py").is_file()

        # Test generated gitignore file
        git_ignore = self.test_folder / ".gitignore"
        assert git_ignore.is_file()
        with git_ignore.open() as f:
            assert "src/sample_module/api" in f.read()

        # Test link to installed venv packages
        assert (self.test_folder / ".nmk" / "protos").exists()

        # Test incremental build
        self.nmk(project, extra_args=["py.format"])
        self.check_logs(["[proto.gen.py]] DEBUG 🐛 - Task skipped, nothing to do", "[py.format]] DEBUG 🐛 - Task skipped, nothing to do"])

        # Test rebuild after proto file touch
        (self.test_folder / "protos" / "sample_module" / "api" / "sample.proto").touch()
        self.nmk(project, extra_args=["py.format"])

    @pytest.fixture
    def with_chdir(self):
        # Change directory to generated project one
        path_to_restore = os.getcwd()
        os.chdir(self.test_folder)

        # Yield to test
        yield

        # Restore previous directory
        os.chdir(path_to_restore)

    def test_check_python_failed(self, with_chdir):
        # Generate python code from proto
        prj = self.prepare_proto_project("python_ko", extra_proto=self.target_proto2("sample_module_ko"), module_name="sample_module_ko")
        self.nmk(
            prj,
            extra_args=["tests"],
            expected_rc=1,
            expected_error="An error occurred during task proto.check.py build: Couldn't build proto file into descriptor pool: duplicate symbol 'FOO'",
        )

        # Retry with disabled check
        self.nmk(prj, extra_args=["proto.check.py", "--config", '{"protoDisableCheck":true}'])
        self.check_logs("/[proto.check.py]] DEBUG 🐛 - Task skipped, nothing to do")

    def test_check_python_ok(self, with_chdir):
        # Generate python code from proto
        prj = self.prepare_proto_project("python_ok", module_name="sample_module_ok")
        self.nmk(prj, extra_args=["tests"])

    def test_check_python_multiple(self, with_chdir):
        # Build a sample project with multiple proto files folders
        folder1 = self.target_proto_folder("sample_module/foo")
        folder1.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(self.template("sample.proto"), folder1 / "sample.proto")
        folder2 = self.target_proto_folder("sample_module/bar")
        folder2.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(self.template("sample2.proto"), folder2 / "sample2.proto")
        prj = self.prepare_project("ref_proto_python.yml")

        # Check generated code
        self.nmk(prj, extra_args=["tests"])
