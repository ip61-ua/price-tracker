from structures import Register
from io import open

class ExportTextFile ():
    def __init__ (self, namefile: str):
        self.namefile = namefile

    def __open (self, mode):
        self.__f = open(self.namefile, mode=mode)

    def __close (self):
        self.__f.close()

    def export (self, data: Register):
        self.__open("w")

        string_output = f"[{data.meta.date_checked}|{data.meta.fetch_response}] <{data.price.current}> {data.product.company} {data.product.name} ({data.meta.origin})"
        self.__f.write(string_output)

        self.__close()

    def read (self) -> str:
        self.__open("r")
        string_input = self.__f.readline()
        self.__close()

        return string_input
