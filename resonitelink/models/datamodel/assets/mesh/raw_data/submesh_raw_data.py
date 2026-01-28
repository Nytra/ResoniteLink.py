from resonitelink.json import abstract_json_model
from dataclasses import field
from typing import Optional, List
from array import array
from abc import ABC, abstractmethod

from dataclasses import InitVar
@abstract_json_model()
class SubmeshRawData(ABC):
    _indices : Optional[bytes] = field(default=None, init=False) # int[]

    @property
    def indices(self) -> List[int]:
        """
        Retrieves the `raw_binary_payload` as list of ints.

        """
        arr = array("i")
        arr.frombytes(self.raw_binary_payload)
        return arr.tolist()
    
    @indices.setter
    def indices(self, indices : List[int]):
        """
        Sets the `raw_binary_payload` from list of ints.
        
        """
        self.raw_binary_payload = array("i", indices).tobytes()
    
    @property
    def raw_binary_payload(self) -> bytes:
        if not self._indices:
            raise ValueError("Binary data was never provided!")
        
        return self._indices

    @raw_binary_payload.setter
    def raw_binary_payload(self, data : bytes):
        expected_len = self.index_count * 4 # 4 bytes per int
        if len(data) != expected_len:
            raise ValueError(f"Expected {expected_len} bytes ({self.index_count} indices * 4 bytes), but got {len(data)} instead!")
        
        self._indices = data

    @property
    @abstractmethod
    def index_count(self) -> int:
        raise NotImplementedError()
