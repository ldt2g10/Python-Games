# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:41:42 2015

@author: Luke
"""

from sys import exit

#List of Game Objects
Key = False
Spear = False


# List of anmials

Bear = True

def dead(why):
    print why, "good Job!"
    exit(0)

def Gold_room():
    print "This room is full of gold, how much will you take:"
    print "1. Pick up as much gold as you can carry."
    print "2. Leave the Gold and turn around and leave"
    
    choice = raw_input(">")
    if choice == "1":
        dead("""While picking up the gold a Monster sneaks up behind you
        and bited your head off""")
    elif choice == "2":
        Bear_room(Spear, Bear)
        
def Bear_room(Spear, Bear):
    if Bear == True:
        print """In front of you is a big black... bear. It stares at you. You
        notice a door behind the bear. To the side of the bear you see a spear propped up against
        the wall. What do you do?"""
        print"1. Fight the bear"
        print"2. Pick up the spear"
        print"3. try to run away"    
        choice = raw_input(">")
        if (choice == "1" and Spear == True and Bear == True) :
            print "You fight and kill the bear. You enter into the next room"
            Bear = False
            Gold_room()
                      
        elif (choice == "1" and Spear == False and Bear == True):
            dead("the bear claws your face off")
        
        
        elif (choice == "2" and Spear == True and Bear == True):
            print "You already have the spear"
            Bear_room(Spear, Bear)
        
        elif (choice == "2" and Spear == False and Bear == True):
            print "you picked up the spear"
            Spear = True
            Bear_room(Spear, Bear)
        
        elif (choice == "3"):
            dead("The Bear catches you and rips your head off")
      
    
        else:
            print "Please choose what to do!"
            Bear_room(Spear, Bear)
    else:
        print "The Bear lies dead on the floor. What do you want to do:"
        print "1. Go into the room full of Gold"
        print "2. return to the room with 3 doors."
        choice = raw_input(">")
        if choice == "1":
            Gold_room()
            
        elif choice == "2":
            Monty_room()
            
        else:
            print "Please input just the number 1 or 2 please"
            Bear_room(Spear, Bear)
                        



def Monty_room():
    print """You enter a room with 3 doors. Above the door
    frames it says 'Monty Hall Project', Please pick which door you would like
       to enter"""
    print "1. Door 1"
    print "2. Door 2"
    print "3. Door 3"
    print "4. Return to where you came from."
    choice = raw_input(">")
    if choice == "1":
        dead("""You open the door. Behind the door is an angry goat. It munches
        your face off""")
    elif choice == "2":
        dead("""You open the door. Behind the door is an angry goat. It munches
        your face off""")
    elif choice == "3":
        print "Well done you picked a door without a goat."
        print "You now enter the next room."
        Bear_room(Spear, Bear)
    
    elif choice == "4":
        Entrance_room(Key)
    else:
        print "Please input 1, 2, 3 or 4 by itself to make a choice"
        Monty_room()
        
           
def Entrance_room(Key):
    print """You are standing inside a castle. Behind you is
    a drawbridge. In front of you is a door. Do you:"""
    print "1. try and open the door"
    print "2. search the room."
    print "3. leave the castle"
    choice = raw_input(">")
    
    if (choice == "1" and Key  == True):
        print "You open the door and go through"
        Monty_room()
        
    elif (choice == "1" and Key == False):
        print "The Door won't Budge!!!"
        Entrance_room(Key)
    
    elif (choice == "2" and Key == False):
        print "You found a key. You pick it up."
        Key = True
        Entrance_room(Key)
        
    elif (choice == "2" and Key == True):
        print "you found nothing else"
        Entrance_room(Key)
    
    elif (choice == "3" and Spear == False):
        dead(""""A wild animal overpowers you on the drawbridge and throws you
        into the water. Glub Glub Glub.... [drowning noises]""")
        
    elif (choice == "3" and Spear == True):
        print """You get attacked by a wild animal. You stab it with your
        spear until it dies. You leave the castle unscathed. You Win!!!"""
    else:
        print "Please input 1, 2 or 3 by itself to make a choice"
        Entrance_room(Key)
        
    
Entrance_room(Key)

#def dead
    
    