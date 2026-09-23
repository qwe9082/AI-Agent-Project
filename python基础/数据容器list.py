# 列表list
# 特点1.可以存储不同类型的元素 2.元素有序、可以重复、元素可以修改
s = [3,67,88, "hello", 1.0, True, None, 88]

#获取
print(s[0]) # 正向索引从0开始
print(s[-8]) # 反向索引从-1开始

print(s[3])
print(s[-5])

# print(s[10]) 超过索引数会报错

# 修改
# s[1] = 10
# print(s)

# 删除
# del s[2]
# print(s)

#列表循环
for item in s:
    print(item)

# 列表切片
print(s[0:6]) # [start:stop:step] 包含start,不包含stop
print(s[0:6:2])
print(s[:6:])
print(s[:6])
print(s[5:-5])

# 列表方法
s.append(True) # 尾部追加元素
s.insert(0,"hello") # 指定索引，插入元素
s.remove("hello") # 移除列表中第一个匹配到的元素
s.pop(2) # 删除指定位置元素，默认0
s.sort() # 列表排序 **数据类型一致才可以排序
s.reverse() #列表反转

print(s)

# 取平均数，sum求和len列表长度
s = [66, 1,2,3]
print(sum(s)/len(s))

print(s)

# 合并列表，并去重
num1,num2 = [11,22,66,88,1,5,9,3],[13,99,45,66,5,45,79]
#合并方法1 列表解包
new_list2 = [*num1, *num2]
print(new_list2)
# 方法2 直接相加
new_list3 = num1 + num2
print(new_list3)
# 合并方法3 循环
for num in num2:
    num1.append(num)
print(num1)
new_num = []
for num in num1:
    if num not in new_num:
        new_num.append(num)
print(new_num)

# 生成1-20的平方列表
# 方法1 循环
mi_list = []
for i in range(1, 21):
    mi_list.append(i**2)
print(mi_list)
# 方法2 列表推导式
mi_list2 = [i**2 for i in range(1, 21)]
print(mi_list2)
