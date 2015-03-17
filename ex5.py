name='Divyansh Agarwal'
age=20 #not a lie
height=178 #cms
weight= 82.0
eyes='Brown'
hair= 'Red'
Teeth='White'


print "Lets talk about %s" %name
print "He is %.1f cms tall" %height
#.1f is used to setprecision to only one place after the decimal
#Here %f converted my integer variable to a floating point number

print "He is %d kgs heavy" %    weight

print "Actually thats not too heavy"

print "He's got %s eyes and %s hair" %(eyes,hair)

print "His teeth are usually %s, but can be yellow sometimes" %Teeth

#THE FOLLOWING LINE IS TRICKY TO GET RIGHT

print "If I add his Height= %d \nWeight= %d\n and divide by the sum of height and weight, we will get his Body mass index\nSum=%d\n" %(height,weight,height+weight)
#Extra line space printed at the end

#IF WE DONT GIVE ENOUGH ARGUMENT AND IDLE LEAVE AN IDLE FORMAT STRING LYING THERE (%d), THEN PYTHON GIVES AN ERROR. 
#I EXPECTED IT TO PRINT A GARBAGE VALUE


#CONVERSIONS:-

#Convert height into inches
#1 inch=2.54 cms

print "\nDivyansh's height in inches is given by %.2r inches\n\n\n" %round(height/2.54)
#Important to put those brackets up there
#round function rounds of the floating point value
#.2f sets prcecision to only two places after the decimal point

















