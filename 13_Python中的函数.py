"""
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。

python 内置:
    print函数   type函数   input函数  open函数

函数的分类:
    参数  返回值
    有参 有返回值
    有参 无返回值
    无参 有返回值
    无参 无返回值
函数的定义:
    def 函数名(参数,参数1,参数2=默认值):
        函数代码块
        [return]

"""
# 求和  有参有返回值
def add(a,b):
    return a+b
# 求和 有参无返回值
def printAdd(a,b):
    print(a+b)

# 无参有返回值
def getStr():
    return "Hello World!!"

# 无参无返回值
def printGood():
    print("好好学习 天天向上!!")

if __name__ == '__main__':
    print(add(10,20))
    printAdd(100,200)
    print(getStr())
    printGood()