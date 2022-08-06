import random

count=100
miles=1000.0
name="johon"
#直接定义并且会进行类型的推断
print(count)
print(miles)
print(name)

# 多字段赋值
a=b=c=d=1
print(a,b,c,d)

# 赋值不同的字段
cd,de,ar=1,2,"json"
print(cd,de,ar)

# 数字类型
var1=1
var2=10

# 字符串

s="asdsf"
print(s[1:4])

str = 'Hello World!'
print("str=",str)
print("str[0]=",str[0])
print("str[2:5]=",str[2:5])
print("str[2:]=",str[2:])
print("str[:5]=",str[:5])
print("str*2=",str*2)
print("str[0]=",str+" Test")
# 多行字符串
a = """Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code."""
print(a)


a = '''Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code.'''
print(a)


# 列表
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print( list  )
print( list[0]  )
print( list[1:3]      )
print( list[2:]   )
print( tinylist * 2      )





x=10
print(type(x))


# 类型转换
a=float(x)
print(type(a))

#随机数
print(random.randrange(1,10))


#指定随机类型
# x = int(1)   # x 将是 1
# y = int(2.5) # y 将是 2
# z = int("3") # z 将是 3
#
# x = str("S2") # x 将是 'S2'
# y = str(3)    # y 将是 '3'
# z = str(4.0)  # z 将是 '4.0'
# bool
print(bool("Hello"))
print(bool(10))