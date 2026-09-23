# 函数
# 注意事项 1.函数必须先定义再调用 2.函数定义时，不会执行，只有在调用时函数体逻辑才会执行 3.函数中通过缩进来描述归属关系
# 函数定义 def
def circle_area(r):
    return 3.14 * r ** 2, round(2 * 3.14 * r, 1)
a, b = circle_area(10)
print(a, b)

# 函数进阶
# 变量作用域
# 1.全局变量: 在函数之外定义的变量，整个文件中都可以使用
# 2.局部变量： 在函数内部定义的变量，只能在该函数中使用

# 传参方式
def sst(name:str, age: int) -> str: # 位置传参 优点：简介 缺点：可读性差、易出错、维护男
    return f"{name}: {age}"
def sst2(name="张三", age=10): # 关键字传参  优点：可读性强、易维护和扩展 缺点：代码繁琐
    return f"{name}: {age}"

print(sst2('李四', 30))
print(sst2(name='李四', age=30))

def calc(*args, **kwargs): # 不定长传参 位置参数会封装成元组 关键字传参会封装成字典
    sum = 0
    for n in args:
        sum += n
    for n in kwargs.values():
        sum += n
    return sum
print(calc(1,2,3,5,five=6, six=8))

add = lambda x, y: x + y # 匿名函数
print(add(1,2))

data:list[str] = ['C', 'C++', 'Python', 'Java', 'Javscript', 'PHP']
data.sort(key = lambda item: len(item))
print(data)
