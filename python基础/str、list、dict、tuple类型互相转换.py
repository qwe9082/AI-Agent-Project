import json
# ‌字符串 → 列表‌：用 split() 按分隔符拆，或用 list() 拆成单个字符
s = "a,b,c"
print(s.split(","))      # ['a', 'b', 'c']
print(list("abc"))       # ['a', 'b', 'c']

# 字符串 → 元组‌：用 tuple() 直接转，每个字符变成元组元素
print(tuple("abc"))      # ('a', 'b', 'c')

# 列表/元组 → 字符串‌：用 join() 拼接，‌要求元素全是字符串
print("".join(['a', 'b']))    # 'ab'
print("-".join(('a', 'b')))   # 'a-b'

# # 列表 → 元组‌：tuple(list)，比如 tuple([1, 2]) 得到(1, 2)
# ‌元组 → 列表‌：list(tuple)，比如 list((1, 2)) 得到 [1, 2]

# ‌字符串 → 字典‌：字符串内容必须是合法的字典格式，用 eval() 或 json.loads()
s = "{'name': '张三', 'age': 18}"
d = eval(s)               # {'name': '张三', 'age': 18}

# 字典 → 字符串‌：用 str() 直接转，或 json.dumps() 转成 JSON 格式
d2 = {'name': '张三'}
print(str(d))             # "{'name': '张三'}"
print(json.dumps(d))      # '{"name": "张三"}'

# 列表与字典互转
keys = ['name', 'age']
values = ['张三', 18]
d = dict(zip(keys, values))    # {'name': '张三', 'age': 18}





