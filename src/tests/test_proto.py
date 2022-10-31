import shutil
from configparser import ConfigParser
from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestProtoPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    @property
    def target_proto(self) -> Path:
        return self.test_folder / "protos" / "sample_module" / "sample.proto"

    def prepare_proto_project(self, other_plugin: str = None) -> Path:
        # Build a sample project with proto files
        self.target_proto.parent.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(self.template("sample.proto"), self.target_proto)
        return self.prepare_project(f"ref_proto{('_'+other_plugin) if other_plugin is not None else ''}.yml")

    def escape(self, to_escape: Path) -> str:
        # Escape backslashes (for Windows paths in json print)
        return str(to_escape).replace("\\", "\\\\")

    def test_version(self):
        self.nmk(self.prepare_proto_project(), extra_args=["version"])

    def test_proto_files(self):
        # Check found proto files
        self.nmk(self.prepare_proto_project(), extra_args=["--print", "protoInputFiles", "--print", "protoInputSubDirs"])
        self.check_logs(f'{{ "protoInputFiles": [ "{self.escape(self.target_proto)}" ], "protoInputSubDirs": [ "sample_module" ] }}')

    def test_python_files_without_python(self):
        # Verify that there are no expected python files without python plugin
        self.nmk(self.prepare_proto_project(), extra_args=["--print", "protoPythonFiles", "--print", "protoPythonSrcFolders"])
        self.check_logs('{ "protoPythonFiles": [], "protoPythonSrcFolders": [] }')

    def test_python_files(self):
        # Verify expected python files
        self.nmk(self.prepare_proto_project("python"), extra_args=["--print", "protoPythonFiles", "--print", "protoPythonSrcFolders"])
        src_path = self.test_folder / "src" / "sample_module"
        self.check_logs(
            f'{{ "protoPythonFiles": [ "{self.escape(src_path/"sample_pb2.py")}", "{self.escape(src_path/"sample_pb2_grpc.py")}", "{self.escape(src_path/"__init__.py")}" ], '
            + f'"protoPythonSrcFolders": [ "{self.escape(src_path)}" ] }}'
        )

    def test_generate_python(self):
        # Generate python code from proto (declared as dependency of python code format)
        project = self.prepare_proto_project("python")
        self.nmk(project, extra_args=["git.ignore", "py.format"])
        src_path = self.test_folder / "src" / "sample_module"
        assert (src_path / "sample_pb2.py").is_file()
        assert (src_path / "sample_pb2_grpc.py").is_file()

        # Test generated gitignore file
        git_ignore = self.test_folder / ".gitignore"
        assert git_ignore.is_file()
        with git_ignore.open() as f:
            assert "src/sample_module" in f.read()

        # Test generated setup file
        setup = self.test_folder / "setup.cfg"
        assert setup.is_file()
        setup_config = ConfigParser()
        setup_config.read(setup)
        assert "src/sample_module" in setup_config["flake8"]["exclude"].split("\n")
        assert "src/sample_module/*" in setup_config["run"]["omit"].split("\n")

        # Test incremental build
        self.nmk(project, extra_args=["py.format"])
        self.check_logs(["[proto.python]] DEBUG 🐛 - Task skipped, nothing to do", "[py.format]] DEBUG 🐛 - Task skipped, nothing to do"])
