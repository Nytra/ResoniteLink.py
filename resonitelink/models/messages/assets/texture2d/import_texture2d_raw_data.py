from resonitelink.models.messages import Message, BinaryPayloadMessage
from resonitelink.json import json_model, json_property
from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod


@dataclass(slots=True)
class ImportTexture2DRawDataBase(BinaryPayloadMessage, ABC):
    width : int = json_property("width", int)
    height : int = json_property("height", int)
    _data : Optional[bytes] = None

    @property
    @abstractmethod
    def element_size(self) -> int:
        raise NotImplementedError()

    @property
    def raw_binary_payload(self) -> bytes:
        if not self._data:
            raise RuntimeError("Binary data was never provided!")
        
        return self._data

    @raw_binary_payload.setter
    def raw_binary_payload(self, data : bytes):
        if not self.width:
            raise ValueError("Width cannot be empty!")
        if not self.height:
            raise ValueError("Height cannot be empty!")

        num_elements = self.width * self.height
        len_bytes = num_elements * self.element_size
        if len_bytes != len(data):
            raise ValueError(f"Data size mismatch: Expected: {len_bytes} bytes, Provided: {len(data)} bytes!")

        self._data = data


@json_model("importTexture2DRawData", Message)
@dataclass(slots=True)
class ImportTexture2DRawData(ImportTexture2DRawDataBase):
    color_profile : str = json_property("colorProfile", str)

    @property
    def element_size(self) -> int:
        return 4 * 1 # color32: 4 * byte


@json_model("importTexture2DRawDataHDR", Message)
@dataclass(slots=True)
class ImportTexture2DRawDataHRD(ImportTexture2DRawDataBase):
    @property
    def element_size(self) -> int:
        return 4 * 4 # color: 4 * float (4 bytes)
