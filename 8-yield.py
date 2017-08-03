import sys

def fibonacci(n): #生成器函数 - 斐波那契
	a,b,counter = 0,1,0
	while True:
		if (counter>n):
			return
			pass
		yield a
		'''
		使用了 yield 的函数被称为生成器
		在调用生成器运行的过程中，
		每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。
		并在下一次执行 next()方法时从当前位置继续运行。
		'''
		a,b=b,a+b
		counter = counter+1
		pass
	pass
f = fibonacci(10)

while True:
	try:
		print (next(f),end=" ")
	except StopIteration:
		sys.exit()