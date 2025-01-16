# a = {1,2,3,1,1,1,1,2,2}
# print(a)
# # for removing duplicates for list using set
# a = [1,2,3,1,1,1,1,2,2]
# print(list(set(a)))

# a = {1,"abc",True,"12341"}
# print(a)
# this_set = {"apple","banana","cherry"}
# for x in this_set:
#     if x =="banana":
#         print(x)
# /////////for empty set///////////
# a = set()
# print(type(a))
# thisset = {"apple","banana","cherry"}
# mylist = ["kiwi","orange"]

# mylist1=("anc","123",22)
# mylist2 = "Hello"
# # thisset.update(mylist)
# # thisset.update(mylist1)
# # thisset.update(mylist2)

# # thisset.remove("banana") 
# thisset.discard("banana")
# print(thisset)

# thisset = {"apple","banana","cherry"}
# thisset.pop()
# print(thisset)

# ///////////////////////Join sets///////////////////
# /////Union////////
# thisset = {"apple","banana","cherry",1}
# mylist = {"kiwi","orange",1,2,1,1,1}

# mylist1={"anc","123",22}
# # myset =thisset.union(mylist,mylist1)
# myset = thisset | mylist | mylist1
# print(myset)

# ///// intersection ///////////
# set1 = {"apple", "banana", "cherry","blackberry"}
# set2 = {"google","microsoft","apple","blackberry"}

# # set3 = set1.intersection(set2)
# set3 = set1 & set2 # "&" for intersection
# print(set3)

# set1 = {"apple", "banana", "cherry","blackberry"}
# set2 = {"google","microsoft","apple","blackberry"}
# set1.intersection_update(set2)
# print(set3)

# set1 = {1,"apple",True, 0}
# set2 = {False,"google","apple",2,True}

# set3 = set1.intersection(set2)
# print(set3)

#///////////// Difference ///////////////
# set1 = {1,"apple",True, 0,"cherry"}
# set2 = {False,"google","apple",2,True}
# set3 = {"apple","banana"}
# # set4 = set1.difference(set2,set3)
# set4 = set1 - set2 - set3 # " - " used for difference
# print(set4)

# set1 = {"apple", "banana", "cherry","blackberry"}
# set2 = {"google","microsoft","apple","blackberry"}
# set1.difference_update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry","blackberry"}
# set2 = {"google","microsoft","apple","blackberry"}
# # set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2 # " ^ " used for symmetric difference
# print(set3)

set1 = {"apple", "banana","cherry" }
set2 = {"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set1)