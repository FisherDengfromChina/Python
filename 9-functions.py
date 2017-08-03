def hello():
	print('hello world')


def area(width,height):
	return width*height
	pass


def print_welcome(name):
	pprint('Welcome,' name)
	pass


def printme(str):
	"Print anything submitted here"
	print (str);
	return
	pass


def changeme(mylist): #修改传入的列表
	mylist.append([1,2,3,4]);
	print ("Inner values of function:",mylist)
	return
	pass
#调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print ("Outter values of function:", mylist)


#不定长参数，以*标识
def printinfo(arg1,*vartuple):
	"Print any values submitted"
	print ("Output:")
	print (arg1)
	for var in vartuple:
		print(var)
	return;
	pass
#调用printinfo函数
printinfo(10)
printinfo(70,60,50)


#匿名函数，用lambda标识
sum = lambda arg1,arg2: arg1+arg2;
print("Added value:",sum(10,20))


#return语句
def sum(arg1,arg2):
	total = arg1+arg2
	print("Inner function:",total)
	return total;
	pass
#调用sum函数
total = sum(10,20);
print ("Outter function:",total)