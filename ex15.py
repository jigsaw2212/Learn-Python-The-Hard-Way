#READING FILES

from sys import argv

script, filename=argv

txt=open(filename)
#Here open returns a file object we store in txt
#Default mode is the write mode

print "Here's your file %r\v" %filename
print txt.read()

txt.close()

#print txt.read(), will give an error after the close() functioin has been called 

#Weird thing- It also reads a file with .py extension in the same directory

print "*" *15 

print "Type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()

txt_again.close()


#So, using the above code, we can output two different files as well
