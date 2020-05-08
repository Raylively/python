# -*- coding: utf-8 -*-

from threading import Thread,current_thread
from time import sleep,time


def process():
    for i in range(3):
        sleep(1)
        print("%d-thread name is %s\n" % (i,current_thread().name))

def main():
    print("-------主线程开始------")
    ts = [Thread(target=process) for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("主线程结束。。。。。。")

if __name__ == "__main__":
    main()
