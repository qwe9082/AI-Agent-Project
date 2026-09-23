import random
# while 判断条件为False跳出循环,else为跳出循环后执行的代码
x = 1
while x < 10:
    x += 1
    # break
    # continue
else:
    x *= 10
print(x)

# while计算1-100之间所有的偶数之和
i = 1
count = 0
while i <= 100:
    if i % 2 == 0:
        count += i
    i += 1
print(count)


# for循环 计算1-100之间所有偶数之和 range(start, stop, step)包含start,不包含stop
count2 = 0
for i in range(0, 101, 2):
        count2 += i
print(count2)

# for循环 打印字符串
h = "Hello World!"
for i in h:
    print(i, end="") # print输出默认\n结束，用end改变输出结束
print()

# 嵌套循环 答应99乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(f"{y} x {x} = {x*y}", end = "\t")
    print()

# 嵌套循环案例
for x in range(1, 9):
    for y in range(1, 9):
        if (x + y) % 2 == 0:
            print("■", end="\t")
        else:
            print("□", end="\t")
    print()

## 使用break可以结束循环，使用continue中断本次循环继续下一次循环
random_num = random.randint(1, 100)
while True:
    num = int(input("请输入数字"))
    if num > random_num:
        num = input("太大")
    elif num < random_num:
        num = input("太小")
    else:
        print("正确!")
        break