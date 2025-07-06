from abc import ABC, abstractmethod

class Storage (ABC):
    @abstractmethod
    def check (self) -> bool:
        pass

    @abstractmethod
    def store (self, data):
        pass

    @abstractmethod
    def store_all (self, data: list):
        pass

    @abstractmethod
    def obtain_all (self) -> list:
        pass
