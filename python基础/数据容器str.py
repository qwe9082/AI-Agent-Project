# 字符串str
# 特点1.无法修改 2.有序性每个字符都有下标 3.可迭代
a ="Hello World!"
print(a[-1:-13:-1]) # 字符串反转
print(a[::-1]) # 字符串反转

# 常用方法
# find 查找对一个出现的字串 s.find("h")
# count 统计字符出现的次数 s.count("h")
# upper 所有字母大写
# lower 所有字母小写
# split 将字符串按指定字符分割成列表 s.split(' ')
# strip 去除两端的空白字符或者指定字符 s.strip() s.strip('*')
# replace 将指定字符替换为新的字符 s.replace('s', 'h')
# startWith 检测是否以指定字符开头 s.startWith('aa')