from resonitelink.json import json_property
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True)
class Message(ABC):
    message_id : str = json_property("messageId", str)


@dataclass(slots=True)
class BinaryPayloadMessage(Message, ABC):
    @property
    @abstractmethod
    def raw_binary_payload(self) -> bytes:
        raise NotImplementedError()

    @raw_binary_payload.setter
    @abstractmethod
    def raw_binary_payload(self, data : bytes):
        raise NotImplementedError()
