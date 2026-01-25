from resonitelink.json import json_element
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

@dataclass(slots=True)
class Message(ABC):
    message_id : str = json_element("messageId", str)


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
