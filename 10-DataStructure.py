'''
list.append(x)	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])		从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()		移除列表中的所有项，等于del a[:]。
list.index(x)		返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)		返回 x 在列表中出现的次数。
list.sort()			对列表中的元素进行排序。
list.reverse()		倒排列表中的元素。
list.copy()			返回列表的浅复制，等于a[:]。
'''

# count
a = [66.25,333,333,1,1234.5]
print(a.count(333),a.count(66.25),a.count('x'))
# Return: 2 1 0
a.insert(2,-1) #在第2位插入数据
a.append(333)
print(a)
# Return: [66.25,333,-1,333,1,1234.5,333]
a.index(333)
# Return: 1
a.remove(333)
print(a)
# [66.25,-1,333,1,1234.5,333]
a.reverse()
print(a)
# Return: [333, 1234.5, 1, 333, -1, 66.25]x
a.sort()
print(a)
# Return: [-1, 1, 66.25, 333, 333, 1234.5]


#将列表作为队列使用
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft() #弹出第一个数据，Return: Eric
queue #Return: deque([John","Michael","Terry","Graham"])


#列表推导式
vec = [2,4,6]
[3*x for x in vec] #Return: [6,12,18]
[[x,x**2] for x in vec] #Return: [[2,4],[4,16],[6,36]]

#对每个元素调用方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']

#使用if子句作为过滤器
[3*x for x in vec if x > 3] #Return: [12,18]

#其他技巧
vec1 = [2,4,6]
vec2 = [4,3,-9]
c #Return: [8, 6, -18, 16, 12, -36, 24, 18, -54]
[x+y for x in vec1 for y in vec2] #Return: [6, 5, -7, 8, 7, -5, 10, 9, -3]
[vec1[i]*vec2[i] for i in range(len(vec1))] #Rtuen: [8, 12, -54]

#使用复杂表达式或嵌套函数
[str(round(335/113),i) for i in range(1,6)] #Return: ['3.1', '3.14', '3.142', '3.1416', '3.14159']


#嵌套列表解析
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
]
[[row[i] for row in matrix] for i in range(4)] #Return: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix]) #row[i]即标识该列的所有数据


#元组
t = (12345,54321,'hello!')
u = (t, (1,2,3,4,5)) #Return: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))


#集合(可用于消除重复的元素)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} #basket = {'orange', 'banana', 'pear', 'apple'}
a = set('abracadabra') #a = {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam') #b = {'a','l','c','z','m'}
a - b #Return: {'r', 'd', 'b'}
a | b #Return: {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b #Return: {'a', 'c'}
a ^ b #Return: {'r', 'd', 'b', 'm', 'z', 'l'}
'orange' in basket #Return: True
'crabgrass' in basket #Return: False
#推导式
a = {x for x in 'abracadabra' if x not in 'abc'} #Return: {'r', 'd'}


#字典
tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4127 #Return: {'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack'] #Return: 4098
del tel['sape']
tel['irv'] = 4127 #Return: {'guido': 4127, 'irv': 4127, 'jack': 4098}
list(tel.keys()) #Return: ['irv', 'guido', 'jack']
sorted(tel.keys()) #Return: ['guido', 'irv', 'jack']
'guido' in tel #Return: True
'jack' not in tel #Return: False

#构造函数
dict([('sape',4193),('guido',4127),('jack',4098)])
dict(sape=4139, guido=4127, jack=4098)

#推导
{x:x**2 for x in (2,4,6)} #Return: {2:4,4:16,6:36}


#遍历技巧
#字典中遍历时，关键字和对应的值可以用items()方法同时解读
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k,v)
	pass
'''
Return: gallahad the pure
	  	robin the brave
'''

#序列中遍历时，索引位置和对应值可以使用enumerate()函数同时得到
for i,v in enumerate(['tic','tac','toe']):
	print(i,v)
'''
Return: 0 tic
		1 tac
		2 toe
'''

#同时遍历两个或更多的序列，可以使用zip()组合
questions = ['name','quest','favorite color']
answers = ['la(ncelot','the holy grail','blue']
for q,a in zip(questions,answers):
	print('What is your {0}? It is {1}.'.format(q,a))
'''
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
'''

#反向遍历
for i in reversed(range(1,10,2)):
	print(i)
'''
Return: 9
		7
		5
		3
		1
'''

#顺序遍历
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
	print(f)
	pass
'''
Return: apple
		banana
		orange
		pear
'''