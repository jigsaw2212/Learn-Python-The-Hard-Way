#Final program in file handling:-
#num=5
#print num

num=input()
print (num,type(num))

from sys import argv
from os.path import exists

script, sourceFile, destFile=argv

print "Here i'm copying the data from one %s file to %s" %(sourceFile,destFile)

fp=open(sourceFile, 'r')
data=fp.read()
#stores all the data from source file into variable 'data'
print "Data in source file:-" 
print data


print "The input file is %d bytes long" %len(data)

fp.close()

print "Does the destination file exist? %r" %exists(destFile)
#exists returns true if the file exists based on its name as the argument

fp=open(destFile,'w+')
fp.write(data)

print "Data in destination file after copying:\n"
fp.seek(0,0)
print fp.read()





