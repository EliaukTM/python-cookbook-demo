# 模块与包

模块与包是任何大型程序的核心，就连 Python 安装程序本身也是一个包。本章重
点涉及有关模块和包的常用编程技术，例如如何组织包、把大型模块分割成多个文件、
创建命名空间包。同时，也给出了让你自定义导入语句的秘籍。

## 构建一个模块的层级包
> 你想将你的代码组织成由很多分层模块构成的包。

在文件系统上组织你的代码，并确保每个目录都定义了一个 init .py 文件。
```python
graphics/
	__init__.py
	primitive/
        __init__.py
        line.py
        fill.py
        text.py
    formats/
        __init__.py
        png.py
        jpg.py
```

一旦你做到了这一点，你应该能够执行各种 import 语句，如下：

```python
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg
```

## 控制模块被全部导入的内容

> 当使用’from module import *‘ 语句时，希望对从模块或包导出的符号进行精确控制。

在你的模块中定义一个变量 all 来明确地列出需要导出的内容。
举个例子:

```python
# somemodule.py
def spam():
	pass
def grok():
	pass
blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']
```

##  使用相对路径名导入包中子模块

> 将代码组织成包, 想用 import 语句从另一个包名没有硬编码过的包的中导入子模块。

使用包的相对导入，使一个的模块导入同一个包的另一个模块举个例子，假设在你
的文件系统上有 mypackage 包，组织如下：

```python
mypackage/
	__init__.py
	A/
		__init__.py
		spam.py
		grok.py
	B/
		__init__.py
		bar.py
```

如果模块 mypackage.A.spam 要导入同目录下的模块 grok，它应该包括的 import
语句如下：

```python
# mypackage/A/spam.py
from . import grok
```

如果模块 mypackage.A.spam 要导入不同目录下的模块 B.bar，它应该使用的 im-
port 语句如下：

```python
# mypackage/A/spam.py
from ..B import bar
```

##  将模块分割成多个文件

> 你想将一个模块分割成多个文件。但是你不想将分离的文件统一成一个逻辑模块时
> 使已有的代码遭到破坏。

程序模块可以通过变成包来分割成多个独立的文件。考虑下下面简单的模块：

```python
# mymodule.py
class A:
	def spam(self):
		print('A.spam')
class B(A):
	def bar(self):
		print('B.bar')
```

假设你想 mymodule.py 分为两个文件，每个定义的一个类。要做到这一点，首先
用 mymodule 目录来替换文件 mymodule.py。这这个目录下，创建以下文件：

```python
mymodule/
    __init__.py
    a.py
    b.py
```

在 a.py 文件中插入以下代码：

```python
# a.py
class A:
    def spam(self):
    	print('A.spam')
```

在 b.py 文件中插入以下代码：

```python
# b.py
from .a import A
class B(A):
	def bar(self):
		print('B.bar')
```

最后，在 init .py 中，将 2 个文件粘合在一起：

```python
# __init__.py
from .a import A
from .b import B
```

如果按照这些步骤，所产生的包 MyModule 将作为一个单一的逻辑模块：

```python
>>> import mymodule
>>> a = mymodule.A()
>>> a.spam()
A.spam
>>> b = mymodule.B()
>>> b.bar()
B.bar
>>>
```



## 利用命名空间导入目录分散的代码

> 你可能有大量的代码，由不同的人来分散地维护。每个部分被组织为文件目录，如
> 一个包。然而，你希望能用共同的包前缀将所有组件连接起来，不是将每一个部分作
> 为独立的包来安装。

在统一不同的目录里统一相同的命名空间，但是要删去用来将组件联合起来
的 \_\_init\_\_.py 文件。假设你有 Python 代码的两个不同的目录如下：

```python
foo-package/
	spam/
		blah.py
bar-package/
	spam/
		grok.py
```

在这 2 个目录里，都有着共同的命名空间 spam。在任何一个目录里都没
有 init .py 文件。
让我们看看，如果将 foo-package 和 bar-package 都加到 python 模块路径并尝试导
入会发生什么：

```python
>>> import sys
>>> sys.path.extend(['foo-package', 'bar-package'])
>>> import spam.blah
>>> import spam.grok
>>>
```

##  重新加载模块

> 你想重新加载已经加载的模块，因为你对其源码进行了修改。

使用 imp.reload() 来重新加载先前加载的模块。举个例子：

```python
>>> import spam
>>> import imp
>>> imp.reload(spam)
<module 'spam' from './spam.py'>
>>>
```

