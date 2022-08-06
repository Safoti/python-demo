#元祖不可修改
thistuple = ("apple", "banana", "cherry")

print(thistuple)



#元祖更改成list 然后修改
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


for x in  thistuple:
    print(x)