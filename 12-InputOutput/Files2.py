f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
	from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
	seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
	seek(x,1) ： 表示从当前位置往后移动x个字符
	seek(-x,2)：表示从文件的结尾往前移动x个字符
from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
f = open('/tmp/foo.txt', 'rb+')
f.write(b'0123456789abcdef') #Return:16
 f.seek(5)  #移动到文件的第六个字节
#Return: 5
f.read(1)
#Return: b'5'
f.seek(-3, 2) #移动到文件的倒数第三字节
#Return: 13
f.read(1)
#Return: b'd'