from resonitelink.models.messages import Message
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@dataclass(slots=True)
@json_model("importTexture2DFile")
class ImportTexture2DFile(Message):
    file_path : Annotated[str, JSONProperty("filePath")] = MISSING
