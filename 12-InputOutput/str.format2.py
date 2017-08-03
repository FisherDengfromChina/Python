import math
print('Approximate Pi is: {}.'.format(math.pi))
print('Approximate Pi is: {!r}.'.format(math.pi))
print('Approximate Pi is: {!s}.'.format(math.pi))
print('Approximate Pi is: {!a}.'.format(math.pi))
#'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化;
#Return: Approximate Pi is: 3.141592653589793;

print('Approximate Pi is: {0:.3f}.'.format(math.pi))
#可选项 ':' 和格式标识符可以跟着字段名;
#Return: Approximate Pi is: 3.142;

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; '
      'Taobao: {0[Taobao]:d}'.format(table))
#Return: Runoob: 2; Google: 1; Taobao: 3

#读取键盘输入
str=input("Please enter: ");
print ("You have entered: ", str)