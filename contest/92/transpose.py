a = [[1,3,4],[2,3,4],[1,4,5]]
print (list((map(list, zip(*a)))))

# *args and **kwargs

def test_var_args(f_arg, *argv):
	print ("first normal arg:", f_arg)
	for arg in argv:
		print ("another arg through *argv :", arg)
	print (list(argv))

test_var_args('yasoob','python','eggs','test')

########
#  **kwargs allows you to pass keyworded variable length of arguments 
#  to a function. You should use **kwargs if you want to handle named 
# arguments in a function. Here is an example to get you going with it:

def greet_me(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print ("%s == %s" %(key,value))

greet_me(name="yasoob")
