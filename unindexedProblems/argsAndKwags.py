#define a function input 
#f return g where g is the square of f
#then define f to be in the form f = x+2

def doubler(f):
	def g(x):
		return f(x) * f(x) 
	return g

def f(x):
	return x + 2

g = doubler(f)
print g(5)