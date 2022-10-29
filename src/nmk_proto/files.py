from pathlib import Path
from typing import List

from nmk.model.resolver import NmkListConfigResolver

from nmk_proto.utils import get_input_proto_files, get_proto_folder


class ProtoFilesFinder(NmkListConfigResolver):
    def get_value(self, name: str) -> List[Path]:
        # Iterate on source paths, and find all proto files
        return list(filter(lambda f: f.is_file(), get_proto_folder(self.model).rglob("*.proto")))


class ProtoSubDirsFinder(NmkListConfigResolver):
    def get_value(self, name: str) -> List[Path]:
        # Filter sub-folders, relative to proto folder
        return list({p.parent.relative_to(get_proto_folder(self.model)) for p in get_input_proto_files(self.model)})
