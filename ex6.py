x="There are %d types of people" 
binary='Binary'

do_not='dont'

y="How many of you know %s and which of you %s" %(binary,do_not)

print x%4 #run time argument
print x%4.0 #Converts float into integer value before printing


print y

print "I said: %r" %x%10
#prints I said: 'There are 10 types of people'
#Like a recursive run time argument! Lol

print "I said: %s" %x%20
#prints I said: There are 10 types of people
#that is without any quotes

print "I also said %s" %y


hilarious=False
joke_eval="Isnt that joke so funny? %r" #evaluates statement to a false
print joke_eval %hilarious #Run time argument

print
#PRINT A LINE BREAK


#NOW I WILL CONCATENATE STRINGS
print "Hello" + x 
#concatenates hello and the string x
print "Hello" + x + "\n"

w="This is the left part of the"
e=" string with right side"

print w+e
#NOTE: You can only concatenate strings using the plus operator






















