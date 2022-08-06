class MyClass:
    x=5


p1=MyClass()

print(p1.x)




class Person:
  def __init__(self,name,age):
      self.name=name
      self.age=age

  def myFunc(self):
    print("hello my name is "+self.name)

p1=Person("Nolo",63)
print(p1.name)
print(p1.age)


p1.myFunc()

p1.age=40
print(p1.age)


# del  p1.age

# print(p1.age)

