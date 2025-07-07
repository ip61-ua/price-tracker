import unittest
from datetime import datetime
import tempfile
from os import path
from io import open
from src.storage.engine.plain_file import PlainFile
from src.model.structures import Register, RegisterMetadata, Price, Product


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.r1 = Register(
            Product("Product Company", "Product Name", "Product Category", 100,
                    "Product ID", "Description Company"),
            Price(50.99, "EUR", 100),
            RegisterMetadata("Engine A", "a.com", 200, datetime(2017, 1, 1, 12, 30)))

    def tearDown(self):
        pass

    def test_file_export(self):
        dst = path.join(self.temp_dir.name, "test1.txt")
        f = PlainFile(dst)
        f.store(self.r1)

        f1 = open(dst, "r")
        s = f1.readlines()
        f1.close()

        self.assertEqual(self.r1.__str__(), s[0][:-1])


if __name__ == '__main__':
    unittest.main()
