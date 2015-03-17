#PLAYING WITH INPUT

print "How old are you?",
age=raw_input()
#Here you are free to input any kind of string

#NOTE: input() function assumes that the input is a valid python expression and return the evaluated result to you

name= raw_input("What is your name?")
#If a prompt argument is present, it is written to standard output wihthout a trailing newline and then the input is read in the same line

print "How old are you?",
age=int(raw_input())
#Now this will only allow an integer input

print "How tall are you?",
height= raw_input()

print "How much do you weigh?",
weight= raw_input()
#The comma ',' after every print is given so that the control of the function doesnt go to the next line, and we can take input in the same line


raw_input()
#This idle raw_input can be used as a getch function before termination. But you have to press enter after it.


print "So you're name is %s, you are %r years old, %r cms tall and weight around %r kgs" % (name,age,height,weight)
#NOTE: %r shows the output in single or double quotes


print "Press any key to terminate"; raw_input()
#But you have to press enter after entering the letter


