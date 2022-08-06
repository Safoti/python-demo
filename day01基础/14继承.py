class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# 使用 Person 来创建对象，然后执行 printname 方法：

x = Person("Bill", "Gates")
x.printname()
class Student(Person):
  def __init__(self, fname, lname):
      Person.__init__(self,fname,lname)
      # super().__init__(fname,lname)
      self.graduationyear = 2019

x = Student("Elon", "Musk", 2019)
print(x)