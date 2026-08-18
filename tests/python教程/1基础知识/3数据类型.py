"""
数据类型
类型转换
1.字符串类型 (String)转整数类型 = int()
2.整数类型 (Integer)转字符串类型 = str()
"""
#字符串转整数
user = int('23872940')
print(user)

#浮点类型转整型
f = 20.4
ff = int(f)
print(ff)

#字符串转浮点型
f = "203.5"
ff = float(f)
print(ff)

#整数转浮点型
i = 20
ff = float(i)
print(ff)

#浮点型转字符串
f = 20.4
ff = str(f)
print(type(ff).__name__)

#整型转字符串
#1.方法是str(int),例如：
f = 30.5
ff = str(f)
print(type(ff).__name__)
#2.type(),语法是 type(对象) ，返回的是对象的类型，前面我们也有用过，但是它是在内部返回的，如果你不输出它你是看不到的，所以经常会和输出函数print()嵌套使用。
f = 30
print(type(f))
#3 isinstance()
#isinstance() 常用来判断数据类型，它返回的是布尔值（True或False），语法是 isinstance(对象,class) 
f = 30.5
print(isinstance(f,int))
