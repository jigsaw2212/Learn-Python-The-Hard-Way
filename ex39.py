#Here we are going to study dictionaries! Dictionaries are nothing but mappings or associations.
#Python dictionaries are also known as associative arrays or has tables

#Creating a mapping of state to abbreviation
states= { 'Oregon': 'OR', 'Florida':'FL', "California":"CA", 
'New York':"NY", "Michigan":'MI' }

print states
#NOTE: This will print the dictionary in any order

#Now map the abbreviated states to the cities
cities={
    'CA':'San Francisco',
    'MI':"Detroit",
    "FL": 'Jacksonville'
    
 }
 
print cities

#add some more cities
cities['NY']='Manhattan'
cities["OR"]='Portland'

print cities
#dictionaries do not give any preference to order! They print randomly

#Let's print out some cities
print '-' *10

print 'Michigan has:' , cities[states['Michigan']]
print 'Florida has:' , cities[states['Florida']]

#print every state abbreviation
print '-' * 10

for x,y in states.items():
    print '%s is abbreviated as %s' %(x, y)
    
'''

for state in states.items():
    print '%s is abbreviated as %s' %(state)
     
    also works, giving the same result!    
    Here we haven't given two different variables for dict.items(), but it still gives the exact same answers
    
    '''
    
    
print states.items()
#dict.items returns all the (key,value) tuples in the form of a list

#print every city in state
print '-' * 10
for city in cities.items():
    print "%s has the city as %s" %city
    

#Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated as %s, and has the city %s"%(state,abbrev,cities[abbrev])

#Now in this case, using only one variable for states.items() won;t work! You will need both the variables


#To fetch a particular value in a dictionary, we use get() function
print '-' * 10
print states.get('Michigan')   #prints MI
state= states.get('Texas')   #prints None

if not(state):
    print 'Sorry, No Texas!'
    

#Assign a default value for some city
city= cities.get('TX','Does not exist in the list')
#^ The format to set default value if some value is not present- get(key, default)
print "The city for states TX is", city

print str(states)

print 'Set of keys in states: ',states.keys()
print 'Set of values in states: ', states.values()


print cities.update(states) #Concatenates two dictionaries; function returns None
print cities

print cities[0]
#Will give an error! You can't access a tuple like this


















