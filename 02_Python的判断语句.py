"""

    if 布尔型的值  [表达式]
        代码
    elif

    else

"""
if __name__ == '__main__':
     # 输入一个学生成绩 要求整数
    score = int(input("请输入成绩"))
    if score >=80:
        print("该学生成绩优秀")
    elif score >= 60 and score < 80:
        print("该学生成绩及格")
    else:
        print("学生不及格")