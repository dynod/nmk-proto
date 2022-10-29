from pathlib import Path
from typing import List

from nmk.model.model import NmkModel


# Get proto source folder from config
def get_proto_folder(model: NmkModel) -> Path:
    return Path(model.config["protoFolder"].value)


# Get input files
def get_input_proto_files(model: NmkModel) -> List[Path]:
    return model.config["protoInputFiles"].value


# Get input sub-folders
def get_input_sub_folders(model: NmkModel) -> List[Path]:
    return model.config["protoInputSubDirs"].value
