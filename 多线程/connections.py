# -*- coding: utf-8 -*-

from threading import Thread,current_thread
from time import sleep,time


def plus():
    print('-------子线程1开始---------')
    global g_num
    g_num += 50
    print("g_num is %d" % g_num)
    print("------子线程1结束---------")

def minus():
    sleep(1)
    print('-------子线程2开始---------')
    global g_num
    g_num += 50
    print("g_num is %d" % g_num)
    print("------子线程2结束---------")

def main():
    print("-------主线程开始------")
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)  
    t1.start()    
    t2.start()
    t1.join()    
    t2.join()    
    print("主线程结束。。。。。。")

if __name__ == "__main__":
    global g_num 
    g_num = 100
    main()
