# -*- coding: utf-8 -*-
from random import randint


#  创建删除集合
s1 = {"python","go","c"}
s2 = {"python",30,r"人生苦短，我用python"}
print(s1)
print(s2)
s3 = set((r"人生苦短",r"我用python"))
print(s3)

s4 = set()   # 空集合，只只能用此此种方式创建

# 添加数据
s4.add("linux")
print(s4)

# 删除元素
s1.pop()
print(s1)   # 移除第一个元素
if "go" in s1:  
    s1.remove("go")  # 移除指定元素
print(s1)
s1.clear()    # 清空集合
print(s1)


# 集合的交集 并集 差集
lang = {"go","python","c","c++"}
lang1 = set(["c++","c","js"])
print(lang & lang1)
print(lang | lang1)
print(lang - lang1)




