#Here we shall implement lists and loops! Get ready

#We start the list with a left square bracket '[', which opens up the list. Then you put each item into the list separated by commas. Lastly, we end with a right square bracket ']' to indicate that its over.

count = [1,2,3,4,5]

print "Count", count
#the list can be printed straight away

fruits= ['apples','pears','banana','Peach','grapes','Oranges']
#List can be of mixed types as well

change=[1, 'pennies',' dimes', 2, 3, 'quarters']

#The first kind of for loop which goes through the count
for i in count: 
    print "The number is %d" %i
    
#Another for loop
for fruit in fruits:
    print "Today we'll have %s" %fruit
    

#Now we'll loop through mixed lists
#We have to use %r as we aren't sure about the contents of the list
for item in change:
    print "I've got a %r" %item
    

elements = []
    
#We can also define empty lists and build them by appending elements to it

#range(i,n) gives us numbers from i to n-1
for i in range(1,6):
    print "Adding %d to the list." %i
    #append is a function that lists can understand, used to add elements to the list
    elements.append(i) 
    #The for loop ends when we start to dedent the statements
    
#Now let's print it put too
for i in elements:
    print "Element list contains: %d " %i
    
print elements.pop()
#Pop function is used to pop an element from the list
#NOTE: By default pop() pops the last element from the list!

#Now lets try and display the list again    
for i in elements:
    print "The new elements contains: %d" %i
    
#We can directly add values like this:-
list2=[]
list2.append(range(5,10))
print list2
#But it creates some troubles while accessing the elements 

print range(10)
#range(n) gives us values from 0 to n-1.   
    
    

