from src.model.structures import Register
from src.storage.storage import Storage
from io import open


class PlainFile(Storage):
    div = '\t'

    def __init__(self, dst: str):
        self.__dst = dst

    def __open(self, mode):
        self.__f = open(self.__dst, mode)

    def __close(self):
        self.__f.close()

    def load(self) -> list[Register]:
        pass

    def store(self, data: Register):
        self.__open("w")
        self.__f.write(data.__str__() + "\n")
        self.__close()

    def store_all(self, data: list[Register]):
        pass

    def check(self) -> bool:
        pass
