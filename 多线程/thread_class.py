# -*- coding: utf-8 -*-

from threading import Thread,current_thread
from time import sleep,time


class Subthread(Thread):
    def run(self):
        for i in range(3):
            sleep(1)
            msg = "子进程" + self.name + "执行，i=" + str(i)
            print(msg)

def main():
    print("-------主线程开始------")
    t1 = Subthread()
    t2 = Subthread()
    t1.start()    
    t2.start()
    t1.join()    
    t2.join()    
    print("主线程结束。。。。。。")

if __name__ == "__main__":
    main()
