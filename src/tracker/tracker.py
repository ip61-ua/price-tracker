from abc import ABC, abstractmethod
from src.model.structures import Register


class Tracker(ABC):
    def __init__(self, link: str):
        self.link = link

    @staticmethod
    def can_parse (link: str) -> bool:
        raise NotImplemented()

    @abstractmethod
    def request (self) -> Register:
        return NotImplemented()

    @abstractmethod
    def request_all (self) -> list[Register]:
        return NotImplemented()

    @abstractmethod
    def request_raw (self) -> str:
        return NotImplemented()

    def get_engine (self) -> str:
        return self.__class__.__name__


class TrackerFactory:
    @staticmethod
    def __cache_save (tracker: Tracker, link: str):
        pass

    @staticmethod
    def __cache_load (link: str) -> (Tracker|None):
        pass

    @staticmethod
    def get_engine_by_link (link: str) -> (Tracker|None):
        pass


