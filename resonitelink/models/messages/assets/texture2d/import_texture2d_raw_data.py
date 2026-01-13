from resonitelink.models.messages import BinaryPayloadMessage
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Annotated, Optional


@dataclass(slots=True)
class ImportTexture2DRawDataBase(BinaryPayloadMessage, ABC):
    width : Annotated[int, JSONProperty("width")] = MISSING
    height : Annotated[int, JSONProperty("height")] = MISSING
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


@json_model("importTexture2DRawData")
@dataclass(slots=True)
class ImportTexture2DRawData(ImportTexture2DRawDataBase):
    color_profile : Annotated[str, JSONProperty("colorProfile")] = MISSING

    @property
    def element_size(self) -> int:
        return 4 * 1 # color32: 4 * byte


@json_model("importTexture2DRawDataHDR")
@dataclass(slots=True)
class ImportTexture2DRawDataHRD(ImportTexture2DRawDataBase):
    @property
    def element_size(self) -> int:
        return 4 * 4 # color: 4 * float (4 bytes)
