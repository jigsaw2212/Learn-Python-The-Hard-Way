from collections import Counter

string1 = "divyansh"

print Counter(string1)
#prints the count of each letter in the string, in a 'key':value format, basically a dictionary format

print #prints a blank line

string2 = "hsyvinad"
print Counter(string2)
#Gives exactly the same code as above!

print string1 == string2
#displays false

print "Are the strings anagrams? :", Counter(string1) == Counter(string2)
#displays true, because it checks the frequency of each letter in the two strings, and finds them to be anagrams

