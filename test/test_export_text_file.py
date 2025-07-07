import unittest
import tempfile
import os
from src.structures import Register, Product, Price, RegisterMetadata
from src.export_text_file import ExportTextFile

class TestExportTextFile(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.r1 = Register(Product("Company A", "Zapatillas con puntera"), Price(12.3, "EUR"), RegisterMetadata("Engine A", "a.com"))
        self.r2 = Register(Product("Taller Paco", "Coche estropeado"), Price(0.21, "EUR"), RegisterMetadata("Engine PacosFerreterria", "paco.com"))
        self.r3 = Register(Product("Dalio Dan Dale Do", "Pinendo 4DS"), Price(350, "EUR"), RegisterMetadata("Engine of bootlegs", "reddit.com"))
        self.r4 = Register(Product("Burbuja de casitas", "Piso en la playa"), Price(39935.50, "EUR"), RegisterMetadata("Engine Home", "escam.com"))

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_1(self):
        dst = os.path.join(self.temp_dir.name, "test_1.txt")
        my_file = ExportTextFile(dst)
        my_file.export(self.r1)
        my_file.export(self.r2)
        my_file.export(self.r3)
        my_file.export(self.r4)
        print (my_file.read())

if __name__ == '__main__':
    unittest.main()
