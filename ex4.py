cars=100
space_in_a_car=4.0
drivers=40
passengers=90.0
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car= passengers/cars_driven


#PYTHON DOESN'T FUCKING PRINT UNTIL YOU TYPE PRINT IN THE STATEMENT

print 'There are',cars ;  print "cars available"
#THE ABOVE CODE PRINTS 'cars available' IN THE NEXT LINE. ';' acts as a delimitor allowing us to put multiple statements on the same line

print "There are",cars,"cars available"
print "There are only",drivers,"Drivers available"
print "There will be",cars_not_driven,"Cars not driven"
print "We have",passengers,"passengers to carpool"
print "We can transport",carpool_capacity,"people today"
print "The average passengers per car is",average_passengers_per_car

#Next statement is alright
print cars + passengers, "END"

#print "There are" + cars + "cars available" - will give an error because we can't concatenate two string and int objects

