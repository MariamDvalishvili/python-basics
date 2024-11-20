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







import unittest

input_age = int(input())


def my_function(age):
    if age > 18:
        return("Du bist erwachsen.")
    elif 6 <= age <= 18:
        return("Du bist ein Teenager.")
    else:
        return("Du bist ein Kind.")

res = my_function(input_age)
print(res)


class TestAgeFunction(unittest.TestCase):
    def test_kind (self):
        self.assertEqual(my_function(50), "Du bist ein Kind.")
    
    def test_teenager(self):
        self.assertEqual(my_function(7), "Du bist ein Teenager.")
    
    def test_erwachene(self):   
        self.assertEqual(my_function(3), "Du bist erwachsen.")


if __name__ == "__main__":
    unittest.main()



