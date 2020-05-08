# -*- coding: utf-8 -*-

from multiprocessing import Queue,Process
from time import sleep


"""
Queue()         # 如果没有指定数量或数量为负，表示可接受的消息数量没有上限
Queue.qsize()   # 返回当前数列包含的消息数量
Queue.full()    # 队列满了返回true,反之false
Queue.get()     # 获取队列中的一条消息，然后将其从队列移除
Queue.put()     # 相对列存消息


"""



def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入:%s"%message)


def read_task(q):
    sleep(1)
    while not q.empty():
        print("读取:%s"%q.get(True,2))

def main():
    print("父进程开始。。。。。。")
    q = Queue()
    pw = Process(target=write_task,args=(q,))
    pr = Process(target=read_task,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("子进程结束。。。。。。")

if __name__ == "__main__":
    main()
