def my_function():
    print("Hello from a function")

# 调用
my_function()


# 函数带参数
def my_funtion(fname):
    print(fname + " Gates")


my_funtion("Bill")
my_funtion("Steve")
my_funtion("Elon")



# 函数参数的默认值

def my_function(country="China"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



# 列表传参


def my_list_function(food):
    for x in food:
        print(x)



fruits = ["apple", "banana", "cherry"]

my_list_function(fruits)





# 返回值的参数

def my_return(x):
    return 5*x

print(my_return(3))
print(my_return(5))
print(my_return(9))



# 如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
# 这样，函数将接收一个参数元组，并可以相应地访问各项：
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Phoebe", "Jennifer", "Rory")
