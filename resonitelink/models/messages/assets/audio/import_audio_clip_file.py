from resonitelink.models.messages import Message
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("importAudioClipFile", Message)
@dataclass(slots=True)
class ImportAudioClipFile(Message):
    pass