import unittest

from src.hello_world import hello_world


class TddHelloWorld(unittest.TestCase):

    def setUp(self):
        hello_world_object = hello_world()
	self.__hello = hello_world_object.say_hello()
       

    def test_say_hello_ok(self):
        self.assertEqual(self.__hello, "Hello World!!")

    def test_say_hello_fail(self):
	hello = "Bye!!"
	self.assertNotEqual(hello, "Hello World!!")

if __name__ == "__main__":

    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()
