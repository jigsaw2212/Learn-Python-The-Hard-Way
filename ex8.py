formatter= '%r %r %r %r'
#%r is used to print anything, regardless of its type


print formatter %(1,2,3,4)
print formatter %('one','two','three','four' )
#prints: 'one','two','three','four',  in quotes 

formatter= '%s %s %s %s'
print formatter %('one','two','three','four' )
#Will print: one two three four, i.e. without quotes

formatter= "%r %r %r %r"

print formatter %(True, False, False,True)
#Can also print boolean values
#Earlier showed *'str' object is not callable* error as I forgot to add the percentage sign above


print formatter %(formatter %(1,2,3,4),formatter,formatter,formatter)
#Update- Here I have again given recursive run time arguments, kinda

print formatter %("Through this exercise",
"I have come to learn",
"the working of",
"the %r formatting style") #Update-%'hello'-  can replace this %r as well :3

#NOTE: %r outputs with single or double quotes randomly!

print
#An idle print statement prints a blank line
