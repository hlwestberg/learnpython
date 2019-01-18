#simple hello world exercise
hi = "hello world"
print(hi)

def add_numbers(a, b):
	"""
	Add two numbers together
	Returns
	--------
	the_sum : type of arguments
	"""
	return a  + b


#practice referencing functions from other files
import some_module
result = some_module.f(5)
pi = some_module.PI

print(result)
print(pi)