#In this exercise, we will implement nested if's

#NOTE: In this program, i'm using input instead of raw_input(), because otherwise i'll have to add double quotes everytime I try to check for the equality, because raw_input() treats the input like a string. But using input won't allow me to enter syntactically incorrect strings

print "You enter a dark room with two doors. Do you wish to go through the door marked #1, or the door marked #2?"

door=input("> ")

if door==1:
    print "You chose door 1, there's a giant bear sitting behind this door"
    print "1. Choose option 1 of nested if"
    print "2. Choose option 2 of nested if"
    
    bear=input("> ")
    
    if bear==1:
        print "The bear eats your face off!"
    
    elif bear==2:
        print "The bear eats your legs off!"
        
    else:
        print "Well maybe doing %s is better" %bear
        #If bear has been inputted as anything other than 1 or 2
        
elif door==2:
    print "You stare into an endless abyss"
    print "1. Blueberries"
    print "2. Blackberries"
    print "3. Just Berries!"
    
    insanity=input("> ")
    
    if insanity == 1 or insanity ==2:
        print "You are not that insane, you can manage i guess"
        
    else:
        print "You are extremely insane my love! You need treatment"
        
else:
    print "You stumble around, fall face flat on a knife and die!"
    
    
       
       
              
       