from resonitelink.models.messages import Message
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@dataclass(slots=True)
@json_model("importTexture2DFile", Message)
class ImportTexture2DFile(Message):
    file_path : str = json_property("filePath", str)
