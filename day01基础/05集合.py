#集合是无序和无索引的集合。在 Python 中，集合用花括号编写。


thisset={"apple", "banana", "cherry"}
print(thisset)


for x in thisset:
    print(x)



print("banana" in thisset)

# 集合一旦创建，您就无法更改项目，但是您可以添加新项目。
# 要将一个项添加到集合，请使用 add() 方法。

# 要向集合中添加多个项目，请使用 update() 方法。

# thisset.add("orange")
# print(thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)
print(len(thisset))
thisset.remove("banana")
print(thisset)

