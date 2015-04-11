#In this self-exercise, i'l perform some operations on ists


print list1.append(10)
#prints None because the function append returns nothing

print list1

print list1.pop() #prints the number popped, as funcion pop() returns the popped number
print list1 


print list1.extend(list2) #extend is used to merge two lists together.
#Although the function doesnt return anything, hence the above statement prints None
print list1

#Now i'll try and insert a string in the above list
list1.append("Hello")
print list1
#It works!

print "Length of list 1:",len(list1)

print list1.insert(6,'start')
#insert also returns None
#insert is of the form insert(index, value)
print list1

print list1.remove('Hello')
#removes the given value from the list
#returns None
print list1

print list1.index(5)
#Returns index at the first occurrence of 5
#This is an important function! Can be used to solve many problems

print "No of times 4 occurs =",list1.count(4)

print list2.reverse()
#reverses the list actually
#returns null
print list2
#printing the reversed list


list1= [1,2,3,4,5]

list2= [6,4,7,1,8,10]

fruits= ['apples','pears','banana','Peach','grapes','Oranges']

print list1.sort()
#sort() function returns Null, actually sorts the list in place
print list1

print "Before sorting:",list2
print sorted(list2)
#Returns the sorted list, but doesn't actually sort the list out!
print "After sorting:",list2
#prints the list similar to the one entered, i.e. without any permanent sort


#reverse is a boolean value which when set to true, reverses the comparisons used to sort the list
print sorted(fruits, key=str.lower, reverse=True)
print fruits
#As expected, the original list fruits remains unchanged

#Specifies a key to sort the values in the list
fruits.sort(key=str.lower)
print fruits







