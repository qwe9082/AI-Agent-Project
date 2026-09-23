# 面向对象 类class
class Car:
    pass

c1 = Car()

c1.name = '兰博基尼'
c1.price = 5000000
c1.color = 'red'

# print(c1)
# print(c1.__dict__) # 将对象的属性以dict输出

# 定义类
class Room:
    street = "江岸路" # 类属性
    type = "住宅"
    # __xx__为魔法方法，不需要手动调用，python会在合适时候自动调用
    def __init__(self, floor, number, area):
        # 实例属性
        self.floor = floor
        self.number = number
        self.area = area
    def __str__(self): # 定义输出
        return f"{self.floor} {self.number} {self.area}"
    def __eq__(self, other): # 判断两个对象是否相对
        return self.floor == other.floor and self.area == other.area
    def __lt__(self, other): # 小于
        return self.area < other.area
    def __le__(self, other): # 小于等于
        return self.area <= other.area
    def __gt__(self, other): # 大于
        return self.area > other.area
    def __ge__(self, other): # 大于等于
        return self.area >= other.area
    def price(self, unit, discount):
        return f"{self.area * unit * discount:.2f}"

r1 = Room(10, '1001', 120)
r2 = Room(10, '1006', 120)
r3 = Room(15, '1503', 160)
print(r1)
total_price = r1.price(30000, 0.9)
print(total_price)
print(r1 == r2)
print(r3 > r1)
print(r1 == r3)





