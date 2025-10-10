import unittest

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

class TestMathOperations(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-8, 7), -56)
        self.assertEqual(multiply(0,29), 0)
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_minus(self):
        self.assertEqual(minus(12, 23), -11)
        self.assertEqual(minus(-15, 8), -23)



if __name__ == '__main__':
    unittest.main()
