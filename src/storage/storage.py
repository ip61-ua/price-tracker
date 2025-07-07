from abc import ABC, abstractmethod
from src.model.structures import Register


class Storage(ABC):
    @abstractmethod
    def check(self) -> bool:
        pass

    @abstractmethod
    def store(self, data: Register):
        pass

    @abstractmethod
    def store_all(self, data: list[Register]):
        pass

    @abstractmethod
    def load(self) -> list[Register]:
        pass
