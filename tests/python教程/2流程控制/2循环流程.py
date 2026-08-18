"""
循环流程：当满足某种条件的时候，重复执行代码块
"""
#while循环
"""
while循环：当满足某种条件的时候，重复执行代码块
while 条件表达式:
    代码块
    循环变量
    while 4 < 5:
    s = int(input("请输入分数:"))
    if 80 >= s >= 60:
        print("及格")
    elif 80 < s <= 90:
        print("优秀")
    elif 90 < s <= 100:
        print("非常优秀")
    else:
        print("不及格")
        if s > 50:
            print("你的分数在60分左右")
        else:
            print("你的分数低于50分")
"""
#while循环(不死循环)
"""
a = 3
while a < 5:
    s = int(input("请输入分数:"))

    if 80 >= s >= 60:
        print("及格")
    elif 80 < s <= 90:
        print("优秀")
    elif 90 < s <= 100:
        print("非常优秀")
    else:
        print("不及格")
        if s > 50:
            print("你的分数在60分左右")
        else:
            print("你的分数低于50分")
    a += 1
print(a)
print("while执行结束了")

"""
#while循环求和
# 请输入一个整数，并计算各个位和 如：321=6

n = int(input("请输入一个整数:"))  # 将字符串转为整型

# sums累加器：m=10 m=10+5

sums = 0

while n != 0:  # 32 #3
    sums = sums + n % 10  # sums=1+2=3+3=6
    n = n // 10  # 32
print(sums)


