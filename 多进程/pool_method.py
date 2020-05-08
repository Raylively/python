# -*- coding: utf-8 -*-

from multiprocessing import Pool
from time import time,sleep
import os 


"""
apply_async()        # 使用非阻塞方式调用（并行执行）
apply()              # 使用阻塞方式调用
close()              # 关闭Pool,使其不接受新的任务
terminate()          # 不管任务是否完成，立即终止
join()               # 主进程阻塞，等待子进程的退出，必须在close或terminate()之后

"""


def task(name):
    print("子进程(%s)执行task %s..."%(os.getpid(),name))
    sleep(1)


def main():

    print("主进程开始。。。。")
    print("父进程PID:%s"%os.getppid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(task,args=(i,)) 
    print("等待所有子进程结束。。。。")
    p.close()
    p.join()
    print("所有子进程结束。")

    print("主进程结束.....")

if __name__ == "__main__":
    main()
