import unittest
from animals.main import getPigAndDogValidator

def test_must_be_a_pig():
    model = getPigAndDogValidator()   
    return model.predict([[1,0,0]])

def test_must_be_a_dog():
    model = getPigAndDogValidator()   
    case2 = [1,1,1]

    testes = [case2]
    return model.predict(testes)
    

class MyTest(unittest.TestCase):
    def test_classification(self):
        self.assertEqual(test_must_be_a_pig(),1)
        self.assertEqual(test_must_be_a_dog(),0)

if __name__ == '__main__':
    unittest.main()