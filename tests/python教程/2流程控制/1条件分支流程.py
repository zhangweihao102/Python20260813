"""
条件分支流程：当达到某种条件的时候才会触发的代码
if 布尔表达式: #如果为真则执行内部的代码块
	代码块

"""
a = 10
b = 20
if a > b:
    print("真")
else:
    print("假")

a = 10
b = 20
c = 30
n1 = a > b and a < c    #a>b为假，a<c为真，假与真为假
n2 = not a < c   #a<c为真，非真则为假
n3 = a > b or a < c     #a>b为假，a<c为真，假或真为真
if n1:
    print("假")
elif n2:
    print("假")
elif n3:
    print("真")

# 多条件分支
s = int(input("请输入分数："))
if  80 >= s >= 60:
    print("及格")
elif 80 < s <= 90:
    print("优秀")
    
elif 90 < s <= 100:
    print("非常优秀")

else:
    print("不及格")
