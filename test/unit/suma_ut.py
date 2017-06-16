import unittest

from src.suma import suma


class TddSuma(unittest.TestCase):

    def setUp(self):
        self.__nueva_suma = suma()
       

    def test_suma_enteros_ok(self):
	resultado = self.__nueva_suma.suma_enteros(3,5)
        self.assertEqual(resultado, 8)

    def test_suma_enteros_fail(self):
	resultado = self.__nueva_suma.suma_enteros(3, 5)
	self.assertNotEqual(resultado, 5)

if __name__ == "__main__":

    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()
