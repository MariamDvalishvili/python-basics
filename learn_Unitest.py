import unittest

def multiplication(x, y):
 return x * y

sume=multiplication(9, 7)
 
result = "The result = " + str(sume)
print(result)

####

def minus(c, d):
 return c - d
 
sume=minus(198, 64)

result = "The result = " + str(sume)
print(result)

####

def add(z, a):
 return z + a

sume=add(90, 678)

result = "The result = " + str(sume)
print(result)


class TestMathFunctions(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(9, 7), 63, "Multiplication failed")

    def test_minus(self):
     self.assertEqual(minus(198, 64), 134, "minus failed")

    def test_add(self):
     self.assertEqual(add(90, 678), 768, "add failed")
     
if __name__ == "__main__":
    unittest.main()
