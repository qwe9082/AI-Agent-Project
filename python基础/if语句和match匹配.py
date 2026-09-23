score = 100

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

day = input("请输入今天星期几")

match day:
    case "1":
        print("星期一")
    case "2":
        print("星期二")
    case "3":
        print("星期三")
    case "4":
        print("星期四")
    case "5":
        print("星期五")
    case "6":
        print("星期六")
    case "7":
        print("星期天")
    case _:
        print("输入错误")
