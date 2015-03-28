print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \nnewline tabs.'
#Here an escape sequence has been used which helps the compiler not confuse over the apostrophe as the end of the string


poem=""" 
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation!
\n\t\twhere there is none.

"""

print "-----------------------------"
print poem
print "-----------------------------"

five= 10-2+3-6
print "This should be five: %s" %five

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates=jars/100
    return jelly_beans, jars, crates
    
start_point =10000
beans, jars, crates=secret_formula(start_point)
#Here we store the values returned by the function in variables which we will print later

print "With a starting point of %d" %start_point
print "We'd have %d beans, %d jars and %d crates" %(beans,jars,crates)

start_point /= 10
#Cascading the divide operator

print "We can also do this way (By directly printing the result):"
print "We'd have %d beans, %d jars and %d crates" %secret_formula(start_point)
#Here we dont need to take the values returned by the function and store it in variables, we directly print them!




