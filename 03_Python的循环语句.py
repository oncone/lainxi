"""

    for循环

    while循环

    1.求1-100的和
"""

# for求和函数
def forSum():
    # 定义和变量
    sum = 0
    for i in range(1, 101):
        sum += i
    print("1-100的和", sum)
    return sum

# while求和函数
def whileSum():
    # 定义和变量
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(sum)
    return sum

# 定义一个 可以指定任意值的求和函数
def sum(max):
    # 定义和变量
    sum = 0
    for i in range(1, max+1):
        sum += i
    print(sum)
    return sum

if __name__ == '__main__':
   whileSum()
   forSum()
   sum(1000)

   a = ["赵","钱","孙","李"]
   b = ["一","二","三","四"]
   list = []
   for n in a :
       for m in b:
           list.append(n+m)
   print(list)
   print(len(list))