#Function and Variables

def cheese_and_crackers(cheese_count, cracker_boxes):
    print "We have %d boxes of cheese" %cheese_count
    print "We have %d boxes of crackers" %cracker_boxes
    print "Man! That's enough for a party!"
    print "Let's get a blanket.\n"
    

print "We can give the arguments to the function directly:-"
cheese_and_crackers(20,30)


print "\nOR, we can use variables from our script:-"
cheese=10
crackers=30

cheese_and_crackers(cheese, crackers)

print "\nWe can even do math inside too:"
cheese_and_crackers(10+10 , 5+6)

print "\nAnd we can combine variables and math too: "
cheese_and_crackers(cheese+50, crackers-2)

print "Now i'll try to take an input from the user"
cheese= raw_input("Enter no of cheese boxes: ")
crackers= raw_input("Enter no of crackers: ")

cheese_and_crackers(int(cheese), int(crackers))
#Type casting the variables into integers. Required because raw_input() converts everything into a string.
#OR, input() will also work!

#------------------------------------------

print "\nI'm gonna try one more way, of directly passing arguments as the user inputs them"
print "Enter values of cheese and crackers boxes respectively:"
cheese_and_crackers(input(), input() )





