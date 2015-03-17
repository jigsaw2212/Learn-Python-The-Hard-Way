#FUNCTIONS RETURNING SOMETHING

#We are making our own math functions for add, subtract, divide, multiply

def add(a,b):
    print "Adding %d + %d " %(a,b)
    return a+b
    

def subtract(a,b):
    print "Subtracting %d - %d " %(a,b)
    return a-b
    
def multiply(a,b):
    print "Multiplying %d * %d " %(a,b)
    return a*b
    
def divide(a,b):
    print "Divide %d/%d " %(a,b)
    return a/b
    
    
print "Let's do some math functions! Yayy!"

age= add(15,5)
height= subtract(184,6)
weight= multiply(44,2)
iq=divide(250,2)

print "Age: %d, Height: %d, Weight= %d, IQ= %d" %(age, height, weight, iq)

#A puzzle that show's the inside out behaviour of function returns

print "Here is a puzzle for you"
what= add(age, (subtract (height, multiply(weight, divide(iq,2)))))

print "That becomes:", what,  "Can you do it by hand?"


print "\nHere's another puzzle to solve: 24 + 100/34 - 1023"

ans= add(24, subtract(divide(100,34),1023))

print "So 24+100/34-1023 = ", ans

#---------------------------------------------

print "You can even enter two numbers to perform some operation on them"
print "Enter numbers now:"

print add(input(),input())
#In the above statement, I pass two values to the add function which I have entered from the keyboard.
#I return the value
#And then print it as soon as I recieve

