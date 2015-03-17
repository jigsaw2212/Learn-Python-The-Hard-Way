#Using argv and raw_input together!

from sys import argv

script, user_name, alias =argv

prompt='->'

print "Hello %s. I am the %s script" %(alias,script)

print "So %s, do you like me?" %alias
like=raw_input(prompt)

print "Where do you live?"
live=raw_input(prompt)

print "What's the name of your computer?"
name=raw_input(prompt)


print """So %s i gather that your computer's name is %r,
you live in %r, its a beautiful place to live!
And i see that you say you %r like me 
P.S. I won't tell anyone that your real name is %r""" %(alias,name,live,like,user_name)

#NOTE: I am telling you again and again, that %r outputs the quotation marks as well, because it outputs data in the raw form
