# -*- coding: utf-8 -*-

from multiprocessing import Process
from time import time,sleep
import os 


"""
is_alive()        # 判断进程是否还在执行
join()            # 是否等待进程实例执行结束，或等待多少秒
start()           # 启动进程实例(创建子进程) 
run()             # 如果没有给定target参数，对这个对象调用start()方法时，将执行对象中的run()方法
terninate()       # 不管任务是否完成，立即停止
name              # 当前进程实例名，默认从Process-1开始，一次递增
pid               # 当前进程实例的pid值
"""


# 继承Process类
class SubProcess(Process):
    # 重写__init__方法
    def __init__(self,interval,name=""):
        Process.__init__(self)       #调用Process父类的初始化方法
        self.interval = interval     # 接收参数interval
        if name:                     # 判断传递的参数name是否存在
            self.name = name 
    
    # 重写Process类的run()方法
    def run(self):
        print("子进程(%s)开始执行，父进程为(%s)"%(os.getpid(),os.getppid()))
        t_start= time()
        sleep(self.interval)
        t_end = time()
        print("子进程(%s)执行时间为%0.2f秒"%(os.getpid(),t_end - t_start))
        
    
def main():
    print("主进程开始。。。。")
    print("父进程PID:%s"%os.getppid())
    p1 = SubProcess(interval=1,name="child_1")
    p2 = SubProcess(interval=2,name="child_2")
    p1.start()
    p2.start()

    print("p1.is_alive=%s"%p1.is_alive())
    print("p1.is_alive=%s"%p1.is_alive())

    print("p1.name=%s"%p1.name)
    print("p1.pid=%s"%p1.pid)
    print("p2.name=%s"%p2.name)
    print("p2.pid=%s"%p2.pid)
    print("等待子进程结束。。。。。")
    p1.join()
    p2.join()
    print("主进程结束.....")

if __name__ == "__main__":
    main()
