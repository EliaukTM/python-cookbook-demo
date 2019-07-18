#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai

"""
你要为需要并发执行的代码创建/销毁线程
"""

# Code to execute in an independent thread
import socket
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create and launch a thread
t = Thread(target=countdown, args=(10,))
t.start()

# 你可以查询一个线程对象的状态，看它是否还在执行
if t.is_alive():
    print('Still running')
else:
    print('Completed')

# 你也可以将一个线程加入到当前线程，并等待它终止：
t.join()

# Python 解释器在所有线程都终止后才继续执行代码剩余的部分。对于需要长时间
# 运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程。

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()


# 后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。除了如上所示的
# 两个操作，并没有太多可以对线程做的事情。你无法结束一个线程，无法给它发送信
# 号，无法调整它的调度，也无法执行其他高级操作。如果需要这些特性，你需要自己
# 添加。比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询
# 来退出。你可以像下边这样把线程放入一个类中：

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()  # Signal termination
t.join()  # Wait for actual termination (if needed)


# 如果线程执行一些像 I/O 这样的阻塞操作，那么通过轮询来终止线程将使得线程
# 之间的协调变得非常棘手。比如，如果一个线程一直阻塞在一个 I/O 操作上，它就永
# 远无法返回，也就无法检查自己是否已经被结束了。要正确处理这些问题，你需要利
# 用超时循环来小心操作线程。例子如下：
class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)  # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
        # Continued processing
        ...
        # Terminated
        return
