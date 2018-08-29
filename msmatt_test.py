import unittest
from mspack import math

class MsPackMathUnitTest(unittest.TestCase):
    def test_sum(self):
        reult=math.sum(10,15)
        self.assertEqual(reult,25)
    def test_mul(self):
        reult=math.mul(10,15)
        self.assertEqual(reult,25)

if __name__=='__main__':
    unittest.main()