thislist=["apple","banana","cherry"]
print(thislist)


print(thislist[1])
print(thislist[-1])


thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])
print(thisList[-4:-1])


# 更改值
thisList[0]="cook"
print(thisList)


# 遍历
for x in thisList:
    print(x)


# 判断是否存在

if "mango" in thisList:
   print("我在里面")


print(len(thisList))


thisList.append("apple")
print(thisList)


# 插入到指定的位置

thisList.insert(1,"oranges")
print(thisList)

