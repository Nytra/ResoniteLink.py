from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True)
class SubmeshRawData(ABC):
    @property
    @abstractmethod
    def indices_count(self) -> int:
        raise NotImplementedError()
