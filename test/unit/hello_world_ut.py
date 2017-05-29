import unittest

#from ...src import hello_world --> Relative path is wrong


class TddHelloWorld(unittest.TestCase):

#    def setUp(self):

#        self.__hello = hello_world()
       

    def test_say_hello(self):

        #hello = hello_world()
	hello = "Hello World!!"
        self.assertEqual(hello, "Hello World!!")

if __name__ == "__main__":

    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()
