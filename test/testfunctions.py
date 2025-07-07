import unittest
from src import functions1, functions2

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(functions1.func1a("A", "B"), "Hello A and B Hi from func2a")

    def test_something_new(self):
        self.assertEqual(functions2.func2b(), 1)

if __name__ == '__main__':
    unittest.main()
