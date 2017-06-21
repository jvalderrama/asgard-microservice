class response:

        def __init__(self, greeting):
		if greeting == "Hello World demo!!":
                	self.__response = "Hello from the world demo!!"
		else:
			self.__response = ""

        def response_to_hello(self):
                return self.__response
