from abc import ABC, abstractmethod
from model.structures import Register
import os
import importlib

class Tracker(ABC):
    @abstractmethod
    def check(self, link: str) -> bool:
        raise NotImplementedError(self.fetch.__str__())

    @abstractmethod
    def fetch(self, link: str) -> (Register|None):
        raise NotImplementedError(self.fetch.__str__())

class TrackerFactory:
    # TODO Mover esto a config
    __sites_folder: str = "sites"
    __memo = {}

    @staticmethod
    def __is_cached(link: str) -> bool:
        return link in TrackerFactory.__memo

    @staticmethod
    def __load(link: str):
        return TrackerFactory.__memo[link]

    @staticmethod
    def __store(link: str, engine: str):
        TrackerFactory.__memo[link] = engine

    @staticmethod
    def list_modules() -> list[str]:
        # el [:-3] quita el ".py" del final
        return [f[:-3] for f in os.listdir(TrackerFactory.__sites_folder) if f.endswith('.py') and f != "__init__.py"]

    @staticmethod
    def get_tracker(link: str):
        if TrackerFactory.__is_cached(link):
            return TrackerFactory.__load(link)


        for module_name in TrackerFactory.list_modules():
            module = importlib.import_module(f"sites.{module_name}")

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and hasattr(attr, "check"):
                    if attr.check(link):
                        s = attr()
                        TrackerFactory.__store(link, s)
                        return s

        raise ValueError(f"No se puede determinar el tracker para el link dado: {link}")
