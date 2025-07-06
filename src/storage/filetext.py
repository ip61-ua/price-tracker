from base_storage import Storage
import io

class FileText(Storage):
    def __init__ (self, namefile: str):
        self.__namefile = namefile

    def __open(self, mode: str):
        self.__f = io.FileIO(self.__namefile, mode)

    def __close(self):
        self.__f.close()

    def store(self, data):
        self.__open('a')
        self.__f.write(data.encode('utf-8'))
        self.__close()

    def check (self) -> bool:
        return True

    def store_all (self, data):
        pass

    def obtain_all (self):
        return []
