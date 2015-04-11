ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print 'Wait! There aren\'t 10 things in the list. Let\'s fix it'

print ten_things

stuff=ten_things.split(' ')
#Here 'stuff' becomes a list. Splits after every space ' '.

print stuff

more_stuff=['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana']

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." %len(stuff)
   
print "There we go", stuff

print "Let's do some things with stuff"

print stuff[0] #prints the second item, i.e. at the index 1
print stuff[-1] #prints out the last item in the list
print stuff.pop()

#join function joins the elements of a list into a string
print '     '.join(stuff) 
string= ' '.join(stuff)
print string
print '#'.join(stuff[3:7])
#joins from the index 3 (4th item) to the index 6 (7th item) items in the list with a '#' between them 
#Basically, join is the opposite of split. Split will break a string into a list, while join will make a string out of the elements in a list.
