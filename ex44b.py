#In this exerices we will explore compositon, in ex441.py we learnt inheritance

class Other(object):
    
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
        
    def altered(self):
        print "OTHER altered()"
        

class Child(object): #NOTE: There's no inheritance here

    def __init__(self):
        self.other = Other()
        #Instantiation of obeject of one class inside another class
        #This is what basically constitutes a composition
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "CHILD override"
        
    def altered(self):
        print "CHILD before altered"
        self.other.altered()
        print "CHILD after altered"
        
son = Child()

son.implicit()
son.override()
son.altered()    
    
