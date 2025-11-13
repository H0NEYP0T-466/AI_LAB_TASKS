mylist=["apple","banana","orange","kiwi","mango"]
print(mylist)
print("printing list with different data types")
listwithdiffDT=["apple",12,True,'A',21.2]
print(listwithdiffDT)
mylist.append("GRAPES")
print(mylist)
print("accessing with indexing")
print(mylist[-1])
print("slicing the list")
print(mylist[1:4])


print("TASK # 1")
tasklist=["MANGO","STUDENT",466,3.14,'X','Y','Z',True,False]
print(tasklist[-7:-1])


tasklist.append("ORANGE")
print(tasklist)
tasklist.reverse()
print(tasklist)
print("Removing an element from the list")
tasklist.remove("ORANGE")   
print(tasklist)
print(type(tasklist))
print(tasklist[2:])
print(tasklist[:4])
print("Updating a index on the list")
print("Before updating")
print(tasklist)
print("After updating")
tasklist[2]="PINEAPPLE"
print(tasklist)
dir(tasklist)
tasklist.insert(2,"WATERMELON")
print(tasklist)
print("Extending a list")
tasklist2=["A","B","C"]
tasklist.extend(tasklist2)
print(tasklist)
print("extending a list upto a specfic range")
newlist=["D","E","F","G","H"]
tasklist2.extend(newlist[2:])
print(tasklist2)

print("Creating a tuple")
mytuple=("apple","banana","orange","kiwi","mango")
print(mytuple)
print(type(mytuple))
print("Tuple with different data types")
tuplewithdiffDT=("apple",12,True,'A',21.2)
print(tuplewithdiffDT)
print(type(tuplewithdiffDT))
print("Accessing tuple with indexing")
print(mytuple[2])
print("Creating a tuple with one element")
onetuple=("apple")
print(onetuple)
print(type(onetuple))
print("Creating a tuple with one element with comma")
onetuple=("apple",)
print(onetuple)
print(type(onetuple))

print("Converting list to tuple")
print("Applying list functions on tuple")
tuple1=(1,2,3,4,5)
list1=list(tuple1)
print(list1)
list1.append(6)
print(list1)
print(type(list1))

print("Starting with sets")
myset={"apple","banana","orange","kiwi","mango"}

print(myset)
print(type(myset))
print("Creating a set with different data types")
setwithdiffDT={"apple",12,True,'A',21.2}
print(setwithdiffDT)
print(type(setwithdiffDT))
print(len(myset))
