# -*- coding: utf-8 -*-
from random import randint

# 创建/删除列表
lst_1 = [1,2,3,4,5,6,7,8,9,10]
lst_2 = []
lst_3 = list(range(10,20,2))
del lst_2    # python自带垃圾回收，因此del 列表不常用
print(lst_1)
print(lst_3)

# 访问列表元素
lst = ["python",29,r"人生苦短，我用python",["go","c++",30]]
print(lst)
print(lst[3])

for i in lst:
    print(i)

for index,item in enumerate(lst):
    print(index,item)

# 添加修改删除元素
lang = ["c","python","java","javascript"]
print(len(lang))
lang.append("linux")

lang[3] = "go"
print(lang)

del lang[3]
print(lang)

lang.remove("linux")
print(lang)

# 对列表进行统计计算
lst = [1,2,3,4,5,6,7,8,9,4,6,7,8,9,3,6,7]
print(lst.index(9))   # 元素首次出现的下标记
print(lst.count(9))   # 元素出现的次数
print(sum(lst))       # 所有元素的和
print(sum(lst[2:9]))


# 列表排序
lst = [1,2,3,4,5,6,7,8,9,4,6,7,8,9,3,6,7]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

lst1 = sorted(lst)
lst1 = sorted(lst,reverse=True)

lst = ["c++","C","java","Javascript","go"]
lst.sort()
print(lst)
lst.sort(key=str.lower)
print(lst)


# 列表推导式
num = [randint(10,100) for i in range(10)]
print(num)

num1 = [ x for x in num if x > 50]
print(num1)
