#Now we introduce the else statement along with if

people =40
cars=40
trucks=40

if cars > people or trucks <= cars:
    print "We should takw cars as cars are greater than people"
elif cars < people:
    print "We shouldnt take cars, as there are fewer cars than people"
    
else:
    print "We can't decide"
    

#We have the liberty to use any kind of complex expression to be evaluated inside the if statement

if trucks > cars:
    print "That's too many trucks compared to cars"
    
elif trucks < cars:
    print "Trucks are less than cars"
else:
    print "\nWe still can't between cars and trucks! Maybe they are equal?"
    
 
if people >= trucks:
    print "\nTrucks are less than or equal to number of people! Yayy! Let's now take the trucks"
else:
    print "Fine! There are far more people than the no of trucks, so lets just stay home >.<"
