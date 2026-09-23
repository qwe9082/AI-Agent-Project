# 字典dict 键值对、key唯一、可修改
# value可以任意数据类型，key不能为可变类型（列入列表、元组、字典）
d = {"x": 1, "y": True, "z": 'Hello'}

# 访问
print(d["x"])

# 添加 键值对
d["o"] = False
print(d)

#删除
d.pop("o")
del d["z"]
print(d)

#修改
d["x"] = 2
print(d)

#查询
# get 根据key获取value d.get("x")
# keys 获取所有的key d.keys()
# values 获取所有的value d.values()
# items 获取所有的key-value键值对 d.items()
print(d.keys())
print(d.values())
print(d.items())

#遍历
for k in d.keys():
    print(f"{k} : {d[k]}")

for item in d.items():
    print(f"{item[0]} {item[1]}")