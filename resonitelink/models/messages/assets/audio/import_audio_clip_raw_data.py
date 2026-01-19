from resonitelink.models.messages import Message, BinaryPayloadMessage
from resonitelink.json import json_model, json_property
from dataclasses import dataclass


@json_model("importAudioClipRawData", Message)
@dataclass(slots=True)
class ImportAudioClipRawData(BinaryPayloadMessage):
    pass