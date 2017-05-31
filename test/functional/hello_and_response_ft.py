import unittest

from src.hello_world import hello_world
from src.response import response

class TddHelloAndResponse(unittest.TestCase):

    def setUp(self):
        hello_world_object = hello_world()
        self.__hello = hello_world_object.say_hello()


    def test_response_to_hello_ok(self):
        response_greeting = response(self.__hello)
        hello_response = response_greeting.response_to_hello()
        self.assertEqual(hello_response, "Hello from the world!!")


if __name__ == "__main__":

    #import sys;sys.argv = ['', 'Test.testName']

    unittest.main()
