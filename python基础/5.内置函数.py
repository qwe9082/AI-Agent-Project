# 1	    abs(x)	返回数字的绝对值；复数返回复数模长
# 2	    aiter(async_iterable)	返回异步可迭代对象的异步迭代器（异步编程）
# 3	    all(iterable)	可迭代对象全部元素为真返回 True，空序列返回 True
# 4	    any(iterable)	可迭代对象任意一个元素为真返回 True，空序列返回 False
# 5	    anext(async_iterator[, default])	获取异步迭代器下一个元素，可设置默认返回值
# 6	    ascii(object)	返回对象可打印 ASCII 字符串，非 ASCII 字符转为 \u 转义序列
# 7	    bin(x)	将整数转为二进制字符串，格式0bxxxx
# 8 	bool([x])	把对象转换布尔类型 True/False
# 9	    breakpoint()	触发 pdb 调试器，设置代码断点调试
# 10	bytearray([source[, encoding[, errors]]])	创建可变字节数组对象
# 11	bytes([source[, encoding[, errors]]])	创建不可变字节对象
# 12	callable(object)	判断对象是否可调用（函数、类返回 True）
# 13	chr(i)	根据 Unicode 编码数字返回对应字符，例chr(65) → 'A'
# 14	classmethod(func)	类装饰器，定义类方法，第一个参数为cls
# 15	compile(source, filename, mode, *args)	编译源码字符串为代码对象，供eval()、exec()执行
# 16	complex([real[, imag]])	创建复数，complex(2, 3)得到(2+3j)
# 17	delattr(object, name)	删除对象的属性，等价于del object.name
# 18	dict(**kwargs)	创建字典对象
# 19	dir([object])	返回对象所有属性、方法名列表；无参数返回当前作用域名称
# 20	divmod(a, b)	返回元组(商,余数)，例divmod(7,2) → (3,1)
# 21	enumerate(iterable, start=0)	枚举，返回(下标,元素)迭代器
# 22	eval(expression[, globals[, locals]])	执行字符串表达式，返回运算结果，仅支持表达式
# 23	exec(object[, globals[, locals]])	执行字符串完整 Python 代码，无返回值，支持多行语句
# 24	filter(function, iterable)	过滤迭代对象，保留函数返回 True 的元素，返回迭代器
# 25	float([x])	将对象转换浮点数
# 26	format(value[, format_spec])	格式化数据，底层对应str.format()
# 27	frozenset([iterable])	创建不可变集合，元素不可增删，可做字典 key
# 28	getattr(object, name[, default])	获取对象属性，属性不存在可设置默认返回值
# 29	globals()	返回当前全局命名空间字典
# 30	hasattr(object, name)	判断对象是否存在指定属性，返回布尔值
# 31	hash(object)	返回对象哈希值，可哈希对象用于字典 key、集合
# 32	help([object])	查看对象交互式帮助文档
# 33	hex(x)	整数转为十六进制字符串，格式0xxxxx
# 34	id(object)	返回对象内存唯一标识（内存地址数字）
# 35	input([prompt])	读取控制台键盘输入，返回字符串
# 36	int([x[, base]])	转为整数；base 指定进制，如int('1010',2)解析二进制
# 37	isinstance(object, classinfo)	判断对象是否属于某个类，支持多类元组
# 38	issubclass(class, classinfo)	判断一个类是否是另一个类的子类
# 39	iter(object[, sentinel])	生成迭代器对象
# 40	len(s)	返回容器（列表、字符串、字典等）元素数量
# 41	list([iterable])	创建列表对象
# 42	locals()	返回当前局部命名空间字典
# 43	map(function, iterable, ...)	将函数依次作用迭代器每个元素，返回结果迭代器
# 44	max(iterable, *args, key=None, default=None)	返回最大值，key 自定义比较规则
# 45	memoryview(obj)	内存视图，直接操作字节内存，不复制数据
# 46	min(iterable, *args, key=None, default=None)	返回最小值
# 47	next(iterator[, default])	获取迭代器下一个元素，迭代耗尽可设置默认值
# 48	object()	返回基础 object 实例，所有 Python 类的顶层父类
# 49	oct(x)	整数转为八进制字符串，格式0oxxxx
# 50	open(file, mode='r', *args)	打开文件，返回文件对象，用于读写文件
# 51	ord(c)	返回单个字符的 Unicode 编码数字，ord('A') →65
# 52	pow(base, exp[, mod])	幂运算；三参数时pow(a,b,m)等价(a**b)%m高效取模
# 53	print(*objects, sep=' ', end='\n', file=..., flush=False)	控制台打印输出
# 54	property(fget=None, fset=None, fdel=None, doc=None)	属性装饰器，实现 get/set 属性控制
# 55	range(start, stop[, step])	生成整数序列，常用于 for 循环
# 56	repr(object)	返回对象官方表示字符串，尽量可 eval 还原对象
# 57	reversed(seq)	返回反向迭代器，反转序列
# 58	round(number[, ndigits])	数字四舍五入，ndigits 设置保留小数位数
# 59	set([iterable])	创建可变集合对象
# 60	setattr(object, name, value)	给对象设置属性值，等价object.name = value
# 61	slice(start, stop[, step])	创建切片对象，等价a[slice(1,5)]等同于a[1:5]
# 62	sorted(iterable, *, key=None, reverse=False)	排序，返回新列表，不修改原数据
# 63	staticmethod(func)	装饰器，定义静态方法，不需要 self/cls 参数
# 64	str(object='')	转为字符串对象
# 65	sum(iterable, /, start=0)	求和，计算可迭代对象数值总和，start 设置初始累加值
# 66	super([type[, object-or-type]])	调用父类的方法，面向对象继承使用
# 67	tuple([iterable])	创建元组对象
# 68	type(object)	返回对象所属类型；type (name,bases,dict) 动态创建类
# 69	vars([object])	返回对象__dict__属性字典，存储对象实例变量
# 70	zip(*iterables, strict=False)	将多个可迭代对象打包配对，返回元组迭代器