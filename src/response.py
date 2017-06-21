class response:

        def __init__(self, greeting):
		if greeting == "Hello World demo mirror ...!!":
                	self.__response = "Hello from the world mirror ...!!"
		else:
			self.__response = ""

        def response_to_hello(self):
                return self.__response
