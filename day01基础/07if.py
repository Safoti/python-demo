a=66
b=200
if b>a:
    print("b is greater than a")




a = 66
b = 66
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 66
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 66
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



a = 200
b = 66
if a > b: print("a is greater than b")


a = 200
b = 66
print("A") if a > b else print("B")



a = 200
b = 66
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 66
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 66
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


x = 52

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误。
a = 66
b = 200
if b > a:
    pass




