#File Handling and Functions

from sys import argv

script, input_file=argv

def print_all(fp):
    print "print_all() called"
    print fp.read()
    
def rewind(fp):
    print "rewind() called"
    fp.seek(0,0)
    
def print_line(l_count, fp):
    print "print_line() called"
    print l_count, fp.readline()
    
    
current_file= open(input_file)
#current_file is the file object

print "First Lets print the whole file:-"
print_all(current_file)
#passing the file object to the function

print "Now let's rewind, kinda like a tape"
rewind(current_file)

print "Let's print three line"

current_line=1
print_line(current_line, current_file)

current_line+=1
print_line(current_line, current_file)

current_line+= 1
print_line(current_line, current_file)

#NOTE: readline() also returns the \n that is in the file being read at the end of that line.


