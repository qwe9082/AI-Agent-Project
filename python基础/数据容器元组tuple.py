# 元组tuple
# 特点1.不可变的序列 2.可以存储不同类型的元素 3.元素可以重复、有序、不可修改
t1 = (1,3,6,12,66,"python", 1.0, True, None)
t2 = 4,'hello',False

# 访问元组
print(t1[4])
print(t1[-5])

# 切片
print(t1[2: 5])
print(t1[5: -2])

# 方法
# count 计算元素出现次数 t1.count(10)
# index 计算元素第一次出现的索引 t1.index(1.0)

# *注意点* 定义单元素元组
t3 = (100) # 此处括号代表表达式
print(type(t3))

t4 = (100,) # 单元组加上逗号

# 基础解包
t5 = (1,2,3,4)
a,b,c,d = t5
print(a,b,c,d)
# 扩展解包 *收集剩余元素封装到列表中
t6 = ('a','b','c','d')
x,*y,z = t6
print(x, y, z)
s, *o = t6
print(s, o)
*p,q = t6
print(p, q)

# 通过元组组包解包交换元素
a = 100
b = 200
c = 300
a,b,c = c,a,b
print(a,b,c)
