
num=10 
num2=20
if num:
    print 'hello'
    
print 10//5
#Floor division. Divide and then round off to the lowest possible value

#A dictionary
dict1= {'x':1,'z':4, 'y':2}
print dict1
#A dictionary stores a key=value mapping of things

#Swapping in python
num, num2=num2, num
print num
print num2
#^This above method can prove to be extremely important! Do learn this, and also list1.index(value), which returns the index at which the value is present

success=[x for x in range(10) if x%2==0 ]
print success

print range(3,10,4)
#Means, print values from 3 to 10 and keep incrementing by 4

#Now i'll use lambda
#Python supports functional programming, in which we pass functions to other functions, lambda makes our job easier by helping us to easily define short anonymous functions which is not directly accessed

sum= lambda x,y: x+y
print sum(2,3)
#prints the value 5

from itertools import *


#the following code gives us all the permutations of list a
a=[1,2,3,4]
print permutations(a)
print list(permutations(a))

exec 'print "Hello"'


with open('output.txt', 'w') as f:
     f.write('Hi there!')

print a
del a #Deletes the variable a from the namespace
#Doing 'print a' now will give an error as python doesn't recognise the variable 'a' anymore




