print raw_input()
#Will again print the input I provided
#Just something I stumbled across

#ANYWAY, MOVING ON -->

from sys import argv

script, filename=argv

print "We are going to erase your file %r" %filename

print "Opening the file...."
target=open(filename, 'w')
#Opening the file in write mode, you cant read from it
#If file doesn't exist, a new blank file will be created


print "Truncating the file! Goodbye! :*"
#target.truncate()
#Do we really need to truncate the file's contents or does the write mode automatically overwrite the file's contents for us? Think about it

print "Give me 3 lines to add to the file" 

line1=raw_input("Line 1: ")
line2=raw_input("Line 2: ")
line3=raw_input("Line 3: ")

print "Now I will add these 3 lines to your file"

target.write(line1+ "\n"+ line2 + "\n" + line3+ "\nEnd of file")
#target.write(line1+ "\n")
#target.write(line2+ "\n")
#target.write(line3+ "\n")
#We can do this or separately give the libebreaks using \n, as write method doesnt add a newline character to the end of string

#Instead of using 3 write statements, we can combine the whole operation in one 



print "And finally we close the file"
target.close()

#NOTE: truncate() function is redundant here, the write mode overwrites the file autmomatically

#DISPLAYING THE CONTENTS OF THE OVERWRITTEN FILE
print "\nNow we will display the contents of the file:"
target=open(filename, 'r')
print target.readline(), 
print target.readline(), 
print target.readline() 
#Opening the file in read mode 
#Displaying contents using readline() function
#readline() gives a line break after printing each line, hence the comma ',' after the first two print statements

print "File name:", target.name
#Prints the name of the file
print "Is the file closed?", target.closed
#Tells us if the file object has been closed or not
print "The File mode is",target.mode
#Prints the mode in which the file has been opened










