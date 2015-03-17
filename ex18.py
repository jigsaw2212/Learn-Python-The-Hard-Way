#And finally we reach functions!
#NOTE: PYTHON DOESNT USE BRACES TO DEFINE SCOPE! IT RATHER USES INDENTATION TO DEFINE SCOPE OF A FUNCTION

#def- keyword used to defien functions

#This one is like our scripts with argv
def print_two (*args): #We can give any no of arguments to *args.
    arg1, arg2, arg3=args #*args basically stores the arguments in an array.
    print "arg1: %r \narg2: %r" %(arg1,arg2) #And we have to unpack them    
                                             #one by one.

#The functions ends when we 'dedent' it


#the above function implementing *args can actually be replaced by two separate arguments
def print_two_again(arg1, arg2): #Helps us skip the "unpacking arguments from args bullshit
    print "\narg1: %r \narg2: %r" %(arg1,arg2) 
    
    
#This function takes only one argument
def print_one(arg1):
    print "Only argument, arg1: %r" %arg1
    
    
#This function is without arguments
def print_none():
    print "I've got no arguments"
  
    
print_two(10,'Sheyril',"Mom")
print_two_again('Divyansh','Sheyril')
print_one('Divyansh')
print_none()

