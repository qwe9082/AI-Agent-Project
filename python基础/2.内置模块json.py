# 🔧 核心方法
# 1.json.dumps(obj)‌：把Python对象（字典、列表等）转成JSON字符串。常用参数：indent（缩进美化）、ensure_ascii=False（保留中文）、sort_keys（按键排序）。
# 2.json.loads(str)‌：把JSON字符串解析成Python对象（通常是字典或列表）。JSON里的true/false/null会变成True/False/None。
# 3.json.dump(obj, fp)‌：把Python对象转成JSON并直接写入文件。需要先打开文件，通常配合open('file.json', 'w')使用。
# 4.json.load(fp)‌：从文件里读取JSON数据并解析成Python对象。通常配合open('file.json', 'r')使用。‌‌
# 带s的是纯内存操作，不涉及文件；不带s的是直接读写文件。‌‌
#
# 🛠️ 其他常用类
# 1.json.JSONEncoder()‌：编码器类，处理自定义对象的序列化。通常继承它并重写default()方法来处理datetime等特殊类型。
# 2.json.JSONDecoder()‌：解码器类，处理自定义反序列化。一般直接用loads()更常见，很少单独用。
# 3.json.JSONDecodeError‌：异常类，解析无效JSON时抛出，用try-except捕获。‌‌