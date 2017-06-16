class suma:

	def __init__(self):
    		pass

	def suma_enteros(self, first_int, second_int):
		try:
			result=first_int + second_int
		except Exception as ex:
			print ex.message()
		return result
