import hashmap

#create a mapping of state to abbreviation
states=hashmap.new()

hashmap.set(states,'Oregon', 'OR')
hashmap.set(states,'Florida', 'FL')
hashmap.set(states,' ', 'CA')
hashmap.set(states,'California', 'CA')
hashmap.set(states,'New york', 'NY')
hashmap.set(states,'Michigan', 'MI')

#create a mapping of states to cities
cities=hashmap.new()

hashmap.set(cities,'CA', 'San Fracisco')

hashmap.set(cities,'MI', 'Detroit')

hashmap.set(cities,'FL', 'Jacksonville')

#add some more cities
hashmap.set(cities,'NY', 'New york')

hashmap.set(cities,'OR', 'Portland')

#print out some cities
print '-' * 10
print "NY state has : %s" %hashmap.get(cities,'NY')
print "OR state has : %s" %hashmap.get(cities, 'OR')

#print out some states
print '-' * 10
print "Michigan's abbreviation is: %s" %hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" %hashmap.get(states,'Florida')


#print every state's abbreviations
print '-' * 10
hashmap.list(states)

#print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state=hashmap.get(states,'Texas')

if not state:
    print "Sorry, No Texas!"
    
    
#Can we do this on one line?
city=hashmap.get(cities, 'TX', "Does not exist")
print "The city for the state 'TX' is: %s" %city






