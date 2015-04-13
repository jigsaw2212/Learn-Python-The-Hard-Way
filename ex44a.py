#Here we will implement Inheritance
#Sub class can implement inheritance in 3 ways:-
#1. Implicitly inherit from base class
#2. Overrride the base class
#3. Alter the functionality of the base class

class Parent(object):
    
    def implicit(self):
        print "Parent implicit()"
        
    def override(self):
        print "Parent override()"
        
    def alter(self):
        print "Parent alter()"

class Child(Parent):
    
    def override(self):
        print "Child override()"
        
    def alter(self):
        print "Child before alter()"
        super(Child, self).alter()
        print "Child after alter()"

#super keyword is used to access a function with the same name in the base (parent) class
        
dad= Parent()
son= Child()

dad.implicit()
son.implicit()
#Son implicitly inherits this function of the parent class

print 
dad.override()
son.override()

print 
dad.alter()
son.alter()


