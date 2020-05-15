# -*- coding: utf-8 -*-
from random import randint

#  创建删除字典

dict1 = {"name":"python","age":30}   
lst1 = [x for x in range(1,11,2)]
lst2 = [x for x in range(2,12,2)]
dict2 = dict(zip(lst1,lst2))
dict3 = dict(name="python",age=30)
dict4 = dict.fromkeys(lst1)
t1 = ("name","age")
lst3 = ["python",30]
dict5 = {t1:lst3}

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5) 

del dict5         # 删除字典
dict4.clear()     # 清空字典

# 访问字典
print(dict3["name"])
print(dict3.get("name"))

# 遍历字典
for item in dict2.items():
    print(item)
for k,v in dict2.items():
    print(k,v)

# 增删改
dict3["type"] = "strong"
print(dict3)
dict3["type"] = "easy"
print(dict3)

if "type" in dict3:
    del dict3["type"]
print(dict3)


# 字典推导式
dict6 = {i:randint(10,100) for i in range(1,10)}
print(dict6)



