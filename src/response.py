class response:

        def __init__(self, greeting):
		if greeting == "Hello World Demo!!":
                	self.__response = "Hello from the world Demo!!"
		else:
			self.__response = ""

        def response_to_hello(self):
                return self.__response
