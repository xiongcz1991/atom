#定义一个列表
bicycles = ["trek","cannordale","redline","specialized"]
#打印列表
print(bicycles)
#访问列表的第一个元素
print(bicycles[0])
#使用列表元素
print(bicycles[1].title())

#操作元素
#1. 修改
print(bicycles)
bicycles[0]="treck"
print(bicycles)
#2. 添加
print(bicycles)
print("在列表末尾添加元素")
bicycles.append("雷诺")
print(bicycles)
print("在列表中间插入元素")
bicycles.insert(1,"hello")
print(bicycles)
#3. 删除
print(bicycles)
print("使用del删除元素")
del bicycles[0]
print(bicycles)
print("使用pop删除元素")
poped_bicycles = bicycles.pop()
print("poped_bicycles")
print(poped_bicycles)
print("bicycles")
print(bicycles)

