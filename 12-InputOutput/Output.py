for x in range(1,11):
	print (repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
	print(repr(x*x*x).rjust(4))
	pass
#rjust()方法用于将字符串靠右，并在左边填充空格