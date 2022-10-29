import sys
from pathlib import Path
from typing import List

from nmk.model.model import NmkModel
from nmk.model.resolver import NmkListConfigResolver
from nmk.utils import run_with_logs
from nmk_base.common import TemplateBuilder

from nmk_proto.utils import get_input_sub_folders, get_proto_folder


# Grab some config items
def get_python_src_folder(model: NmkModel) -> Path:
    return Path(model.config["pythonSrcFolders"].value[0])


def get_python_out_folders(model: NmkModel) -> List[Path]:
    return model.config["protoPythonSrcFolders"].value


class OutputFoldersFinder(NmkListConfigResolver):
    def get_value(self, name: str) -> List[Path]:
        # Do we have a python source folder?
        if "pythonSrcFolders" in self.model.config:
            # Grab some variables values
            target_src = get_python_src_folder(self.model)
            return [target_src / p for p in get_input_sub_folders(self.model)]
        else:
            return []


class OutputFilesFinder(NmkListConfigResolver):
    def get_value(self, name: str) -> List[Path]:
        # Do we have python output folders
        output_folders = get_python_out_folders(self.model)
        if len(output_folders):
            # Grab some variables values
            target_src, proto_src = (get_python_src_folder(self.model), get_proto_folder(self.model))

            # Convert source proto file names to python ones
            return [
                target_src / f"{str(p_file)[:-len(p_file.suffix)]}{suffix}.py"
                for p_file in [Path(p).relative_to(proto_src) for p in self.model.config["protoInputFiles"].value]
                for suffix in ["_pb2", "_pb2_grpc"]
            ] + [p / "__init__.py" for p in output_folders]
        else:
            return []


class OutputFoldersFinderWithWildcard(OutputFoldersFinder):
    def get_value(self, name: str) -> List[Path]:
        # Same than parent, with a "*" wildcard
        return [p / "*" for p in super().get_value(name)]


class ProtoPythonBuilder(TemplateBuilder):
    def build(self, init_template: str):
        # Grab some config items
        target_src, proto_src, out_folders = (get_python_src_folder(self.model), get_proto_folder(self.model), get_python_out_folders(self.model))
        target_src.mkdir(parents=True, exist_ok=True)

        # Iterate on inputs (proto files)
        for proto_file in self.inputs:
            # Delegate to protoc
            run_with_logs(
                [
                    sys.executable,
                    "-m",
                    "grpc_tools.protoc",
                    "--proto_path",
                    str(proto_src),
                    "--python_out",
                    str(target_src),
                    "--grpc_python_out",
                    str(target_src),
                    str(proto_file),
                ]
            )

        # Reorder output files
        importable_files = {out_folder.relative_to(target_src): [] for out_folder in out_folders}
        for candidate in [p.relative_to(target_src) for p in filter(lambda f: f.name.endswith("_pb2.py"), self.outputs)]:
            importable_files[candidate.parent].append(candidate.as_posix()[: -len(candidate.suffix)].replace("/", "."))

        # Generate init files
        for p, modules in importable_files.items():
            self.build_from_template(Path(init_template), target_src / p / "__init__.py", {"modules": modules})
