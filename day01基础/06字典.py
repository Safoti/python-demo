# 字典是一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值。


thisdict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
print(thisdict)


x=thisdict["model"]
print(x)


u=thisdict.get("year")
print(u)



# 修改值
thisdict["year"]=2019

print(thisdict)


# 遍历

for x in thisdict:
    print(x)



for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
 print(x)

for x in thisdict.keys():
 print(x)


for x ,y in thisdict.items():
  print(x,y)




if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


print(len(thisdict))

thisdict['color']="red"

print(thisdict)

# 复制
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)


myfamily = {
  "child1" : {
    "name" : "Phoebe Adele",
    "year" : 2002
  },
  "child2" : {
    "name" : "Jennifer Katharine",
    "year" : 1996
  },
  "child3" : {
    "name" : "Rory John",
    "year" : 1999
  }
}
print(myfamily)