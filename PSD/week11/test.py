import unittest
import doctest 

def multiply(x, y):
    """Returns the mutiply of two numbers.
    >>> multiply(5,3)
    15
    >>> multiply(-8,7)
    -56
    """
    return x * y

def add(x, y):
    """Returns the mutiply of two numbers.
    >>> add(2,3)
    5
    >>> add(-1,1)
    0
    """
    return x + y

def minus(x, y):
    """Returns the minus of two numbers.
    >>> minus(12, 23)
    -11
    >>> minus(-15, 8)
    -23
    """
    return x - y

def divide(x, y):
    """Returns the divident of two numbers.
    >>> divide(24, 2)
    12
    >>> divide(-15, 0)
    -15
    """
    return x / y 

def remainder(x, y):
    """Returns the remainder of two numbers.
    >>> remainder(24, 5)
    4
    >>> remainder(-15, 2)
    1
    """
    return x % y




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

    def test_divide(self):
        self.assertEqual(divide(24,2), 12)
        self.assertEqual(divide(-15,0), 0)

    def test_remainder(self):
        self.assertEqual(remainder(24,5), 4)
        self.assertEqual(remainder(-15,2), 1)



if __name__ == '__main__':
    unittest.main(exit=False)
    doctest.testmod(verbose=True)


