#Here we begin to learn about classes and objects



class song(object): #its important to write the keyword 'object'."object" lowercased, is the "class" that you inherit from to make a class.
    song='interesting'
    arr=[1,2,3,4]  #An array as an attribute
    
    def __init__ (self,lyrics,default='Lol'): #two underscores in init
        self.name='Random musician:' #name automatically becomes an attribute of class 'song'
        self.lyrics = lyrics
        
        #If init function is not written, the error message says object() takes no parameters
        
        
    def print_lyrics(self):
        random='Hello' #But this can't become an attribute!
        print random #Can be printed just like that, but not as an attribute of the object calling the function
        print self.name, #',' to keep the next print statement on the same line
        print self.lyrics
   
song('Class song acting like an object').print_lyrics()  
#using a class like an object
    
one_last_breath = song(["Hold me now!","I'm 6 ft from the edge"]) 
#Above is the process of instantiation
#Passing the song lyrics in the form of a list so that we can print successive lines in the next line
one_last_breath.print_lyrics()    

america= song('America, dont you cry!')
america.print_lyrics()
print america.name 

print america.arr

#print america.random
#will give an error, because random is not an attribute of object 'america'

import random

print random.randint(1,10)
#gives a  random integer between 1 and 3



