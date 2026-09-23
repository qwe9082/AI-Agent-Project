# 异常 异常捕获
try:
    print(a)
    # 可能出现的异常业务代码
except Exception as err:
    # 出现异常时的预案
    print(f"程序出现错误{err}")
finally:
    # 最终执行
    print("执行完毕")