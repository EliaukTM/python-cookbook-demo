#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : haymai


# 通常情况下，你没有办法
# 知道接收数据的线程是什么时候接收到的数据并开始工作的。不过队列对象提供一些
# 基本完成的特性，比如下边这个例子中的 task done() 和 join()


from queue import Queue
from threading import Thread


# A thread that produces data
def producer(out_q):
    while running:
        # Produce some data
        ...
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        ...
        # Indicate completion
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
# Wait for all produced items to be consumed
q.join()
