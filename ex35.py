from sys import exit
#exit will be used to terminate the program at will

def gold_room():
    print "This room is full of gold. How much gold do you want?"
    how_much=0
    amount = raw_input("> ")
    if "0" in amount or "1" in amount:
        how_much = int(amount)
        #Type casting being done here!
       
    
    if how_much < "50":
        print ("Nice bwoy! You're not greedy, you win!")
        exit(0)
        
    else:
        dead("Man, learn to type a number for Christsake!")
        
def bear_room():
    print "There is a bear here."
    print "Some more bullshit."
    print "How are you going to move the bear?"
    print "You can 'open door', 'taunt bear' or 'take honey'"
    bear_moved= False
    
    while True:
        choice = raw_input("> ")
        if choice == "take honey":
            dead("The bear slaps you to death")
        elif choice== "taunt bear" and not bear_moved:
            print "The bear has been successfully moved. You're a hero"
            bear_moved=True
            
        elif choice== 'taunt bear' and bear_moved:
            dead("The bear gets pissed off and kicks you")
        elif choice=='open door' and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means!"
            
    

def dead(why):
    print why, "You deserved to die, bitch"
    exit(0)
    
def start():
    print "Choose one room"
    choice = raw_input("> ")
    
    if choice == 'left':
        gold_room()
    
    elif choice == 'right':
        bear_room()
    
    else: 
        dead("You stumble around the room, hit your head and die")
    
        
start()   


