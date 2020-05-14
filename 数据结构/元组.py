# -*- coding: utf-8 -*-

from random import  randint

"""
元祖： 不可表列表
      不能修改单个元素，但是可以对整个元祖重新赋值
"""

# 创建元祖
t1 = (1,2,3,4,5,6)
t2 = ("c","java","python","go")
t3 = ("我是一个字符串")
t4 = ("我是一个元祖",)
t5 = ()   # 空元祖
t6 = (range(10,20,2))
del t5    # 不常用

# 元祖推导式,结果是一个生成器
t = (randint(10,100) for _ in range(10))
t = tuple(t)
print(t)

l = [randint(10,100) for _ in range(10)]
print(l)



