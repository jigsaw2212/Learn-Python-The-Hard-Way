def break_words(stuff):
    """This function will break up words for us."""
    #The above string is called as a documentation commen
    
    words =stuff.split(" ")
    #split function splits the sentence into words
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    #This function sorts the 'list' of words
    
def print_first(words):
    """Prints the first word after popping it off."""
    word=words.pop(0)
    print word
    
    
def print_last(words):
    """Prints the last word after popping it off."""
    word=words.pop(-1)
    print word
    
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted order of words."""
    words=break_words(sentence)
    return sort_words(words)
    

def print_first_and_last(sentence):
    """aaaaaaaaaaaaTakes in a sentence and prints the first and the last words."""
    words= break_words(sentence)
    print_first(words)
    print_last(words)
    return
    
def print_first_and_last_sorted(sentence):
     """Prints the first and last words of a sentence after sorting them."""
     words=break_words(sentence)
     print_first(sort_words(words))
     print_last(sort_words(words))
     
   
     print "\nOr we can do by calling the sort_sentence function"
    
     print_first(sort_sentence(sentence))
     print_last(sort_sentence(sentence))
     return
    
    
#While executing from command prompt, we have to write ex25.function_name, if we just normally import ex25. If we don't want to write 'ex25.' all the time, we will do- from ex25 import *, which will import all the functions into that python execution.

#I am not able to remove the recurring Nones upon execution of this code
#Solved it! Actually one of my functions wasnt returning anything and I was still trying to print the values returned! :p
    
    
    
    

