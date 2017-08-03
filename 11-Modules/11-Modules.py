#使用Python标准库中模块的例子
import sys
print('命令行参数如下：')
for i in sys.argv:
	print(i)
	pass
print('\n\nPython is at ',sys.path, '\n')
#import sys引入Python标准库中的sys.py模块，这是引入某一模块的方法；
#sys.argv是一个包含命令行参数的列表；
#sys.path包含了一个Python解释器自动查找所需模块的路径的列表；
#如需在另一Python源文件中执行Python原文建，只需只用import语句即可，该语句将自动在sys.path中搜索模块；


#from...import语句，用于从模块中导入指定的部分
from modname import name1[,name2[,...nameN]]
from modname import * #将所有内容导入
#导入时可包括可执行代码，一般用于初始化，只在第一次被导入时执行；


#__name__属性
#模块被引入时其中的主程序将运行，使用该属性将使程序块仅在该模块运行时执行；
if __name__ = '__main__':
	print('Applicatoin is running')
else:
	print('This is from another module')
#每个模块都有一个__name__属性，当其值为'__main__'时表明该模块自身在运行，否则是被引入的；

#dir()函数
#可以找打模块内定义的所有名称并以一个字符串列表的形式返回；
import sys
dir(sys)


#包
#A.B，即A模块中的B子模块，导入方法不同调用方法也不同，如；
import A.B #调用： A.B.func
from A import B #调用：B.func
from A.B import func #调用：func

#导入*
#可在模块的__all__属性中确定导入的*指哪些子模块；