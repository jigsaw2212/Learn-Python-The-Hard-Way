#This exercise talks about giving run time arguments

from sys import argv
#argv or argument variable contains the list of command line arguments given to the python script when we run it

script,first, second, third=argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third

#It is fine if I have added a fourth run time argument but not printed it. 
#You only get an error when  you do not provide all the required number of arguments and you're trying to use them
#You also cant give too many run time arguments when there are lesser no of argv variables

#NOTE: In python we can print any variable directly as well, with just the print statement

#I ALSO TRIED THE FOLLOWING:-
#Only wrote script=argv
#and then you can write any no of runtime arguments
#jigsaw:Python$ python ex13.py hello i am divyansh
#The script is called: ['ex13.py', 'hello', 'i', 'am', 'divyansh']



