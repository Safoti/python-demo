fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(10):
  print(x)

for x in range(3, 50, 6):
  print(x)


for x in range(10):
  print(x)
else:
  print("Finally finished!")



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
