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

##  运行目录或压缩文件

>您有已经一个复杂的脚本到涉及多个文件的应用程序。你想有一些简单的方法让用
>户运行程序。

如果你的应用程序已经有多个文件，你可以把你的应用程序放进它自己的目录并添
加一个 main .py 文件。举个例子，你可以像这样创建目录：

```
myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py
```

如果 main .py 存在，你可以简单地在顶级目录运行 Python 解释器：

```
 python3 myapplication
```

解释器将执行 main .py 文件作为主程序。
如果你将你的代码打包成 zip 文件，这种技术同样也适用，举个例子：

```
zip -r myapp.zip *.py
python3 myapp.zip
```

## 读取位于包中的数据文件

>你的包中包含代码需要去读取的数据文件。你需要尽可能地用最便捷的方式来做这
>件事。

假设你的包中的文件组织成如下：

```
mypackage/
    __init__.py
    somedata.dat
    spam.py
```

现在假设 spam.py 文件需要读取 somedata.dat 文件中的内容。你可以用以下代码
来完成：

```
# spam.py
import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
```

由此产生的变量是包含该文件的原始内容的字节字符串。

## 将文件夹加入到 sys.path

>你无法导入你的 Python 代码因为它所在的目录不在 sys.path 里。你想将添加新目
>录到 Python 路径，但是不想硬链接到你的代码。

有两种常用的方式将新目录添加到 sys.path。第一种，你可以使用 PYTHONPATH
环境变量来添加。例如：

```bash
bash % env PYTHONPATH=/some/dir:/other/dir python3
Python 3.3.0 (default, Oct 4 2012, 10:17:33)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/some/dir', '/other/dir', ...]
>>>
```

第二种方法是创建一个.pth 文件，将目录列举出来，像这样：

```
# myapplication.pth
/some/dir
/other/dir
```

## 通过钩子远程加载模块

> 你想自定义 Python 的 import 语句，使得它能从远程机器上面透明的加载模块。

我们开始先构造下面这个 Python 代码结构：

```
testcode/
    spam.py
    fib.py
    grok/
        __init__.py
        blah.py
```

这些文件的内容并不重要，不过我们在每个文件中放入了少量的简单语句和函数，
这样你可以测试它们并查看当它们被导入时的输出。例如：

```python
# spam.py
print("I'm spam")

def hello(name):
	print('Hello %s' % name)

# fib.py
print("I'm fib")
def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)
    
# grok/__init__.py
print("I'm grok.__init__")

# grok/blah.py
print("I'm grok.blah")
```

这里的目的是允许这些文件作为模块被远程访问。也许最简单的方式就是将它们发
布到一个 web 服务器上面。在 testcode 目录中像下面这样运行 Python：

```bash
bash % cd testcode
bash % python3 -m http.server 15000
Serving HTTP on 0.0.0.0 port 15000 ...
```

服务器运行起来后再启动一个单独的 Python 解释器。确保你可以使用 urllib 访
问到远程文件。例如：

```python
>>> from urllib.request import urlopen
>>> u = urlopen('http://localhost:15000/fib.py')
>>> data = u.read().decode('utf-8')
>>> print(data)
# fib.py
print("I'm fib")

def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)
>>>
```

加载远程模块的第一种方法是创建一个显示的加载函数来完成它。例如：

```python
import imp
import urllib.request
import sys

def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod
```

这个函数会下载源代码，并使用 compile() 将其编译到一个代码对象中，然后在
一个新创建的模块对象的字典中来执行它。下面是使用这个函数的方式：

```python
>>> fib = load_module('http://localhost:15000/fib.py')
I'm fib
>>> fib.fib(10)
89
>>> spam = load_module('http://localhost:15000/spam.py')
I'm spam
>>> spam.hello('Guido')
Hello Guido
>>> fib
<module 'http://localhost:15000/fib.py' from 'http://localhost:15000/fib.py'>
>>> spam
<module 'http://localhost:15000/spam.py' from 'http://localhost:15000/spam.py'>
>>>
```

更高深的略，可参看书籍

## 安装私有的包

>你想要安装一个第三方包，但是没有权限将它安装到系统 Python 库中去。或者，
>你可能想要安装一个供自己使用的包，而不是系统上面所有用户。

Python 有一个用户安装目录，通常类似”˜/.local/lib/python3.3/site-packages”。要
强制在这个目录中安装包，可使用安装选项“–user”。例如：

```bash
python3 setup.py install --user
```

或者

```shell
pip install --user packagename
```

在 sys.path 中用户的“site-packages”目录位于系统的“site-packages”目录之前。
因此，你安装在里面的包就比系统已安装的包优先级高（尽管并不总是这样，要取决
于第三方包管理器，比如 distribute 或 pip）。

## 创建新的 Python 环境

> 你想创建一个新的 Python 环境，用来安装模块和包。不过，你不想安装一个新的
> Python 克隆，也不想对系统 Python 环境产生影响。

你可以使用 pyvenv 命令创建一个新的“虚拟”环境。这个命令被安装在 Python
解释器同一目录，或 Windows 上面的 Scripts 目录中。下面是一个例子：

```bash
bash % pyvenv Spam
bash %
```

传给 pyvenv 命令的名字是将要被创建的目录名。当被创建后，Span 目录像下面这
样：

```
bash % cd Spam
bash % ls
bin include lib pyvenv.cfg
bash %
```

在 bin 目录中，你会找到一个可以使用的 Python 解释器：

```python
bash % Spam/bin/python3
Python 3.3.0 (default, Oct 6 2012, 15:45:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pprint import pprint
>>> import sys
>>> pprint(sys.path)
['',
'/usr/local/lib/python33.zip',
'/usr/local/lib/python3.3',
'/usr/local/lib/python3.3/plat-darwin',
'/usr/local/lib/python3.3/lib-dynload',
'/Users/beazley/Spam/lib/python3.3/site-packages']
>>>
```

这个解释器的特点就是他的 site-packages 目录被设置为新创建的环境。如果你要
安装第三方包，它们会被安装在那里，而不是通常系统的 site-packages 目录。

## 分发包

> 你已经编写了一个有用的库，想将它分享给其他人。

如果你想分发你的代码，第一件事就是给它一个唯一的名字，并且清理它的目录结
构。例如，一个典型的函数库包会类似下面这样：

```
projectname/
    README.txt
    Doc/
		documentation.txt
    projectname/
        __init__.py
        foo.py
        bar.py
    utils/
        __init__.py
        spam.py
        grok.py
    examples/
    	helloworld.py
    ...
```

要让你的包可以发布出去，首先你要编写一个 setup.py ，类似下面这样：

```python
# setup.py
from distutils.core import setup

setup(name='projectname',
    version='1.0',
    author='Your Name',
    author_email='you@youraddress.com',
    url='http://www.you.com/projectname',
    packages=['projectname', 'projectname.utils'],
)
```

下一步，就是创建一个 MANIFEST.in 文件，列出所有在你的包中需要包含进来的
非源码文件：

```ini
# MANIFEST.in
include *.txt
recursive-include examples *
recursive-include Doc *
```

确保 setup.py 和 MANIFEST.in 文件放在你的包的最顶级目录中。一旦你已经做了
这些，你就可以像下面这样执行命令来创建一个源码分发包了：

```bash
% bash python3 setup.py sdist
```

它会创建一个文件比如”projectname-1.0.zip” 或“projectname-1.0.tar.gz”, 具体
依赖于你的系统平台。如果一切正常，这个文件就可以发送给别人使用或者上传至
Python Package Index.