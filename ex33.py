#Introducing while loop

#Note- A ':' tells a python to start a new block of code, you need to start indenting from there on.


numbers=[]
#empty list

def func(count,inc):
    i=0
    while i < count:
        print "At the top i is %d" %i
        numbers.append(i)
        
        i+=inc
        
        print "Numbers now:",numbers
        print "At the bottom of while loop, i is %d" %i
        
        if(i==count):
            print "\nThis is the end of while loop! Bye bye!" 
    

count= input("Enter Count->")
inc= input("Enter incrementer->")
func(count, inc)

    
print "The numbers are:",

for num in numbers:
    print num 
    

