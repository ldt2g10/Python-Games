# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:45:35 2015

@author: Luke
"""
from sys import exit

#List of Game Objects (to stop python Error and so easy to see objects available in game)
spear = False
def dead(why):
    print why, "good Job!"
    exit(0)
    
def bear_room(spear):
    print """In front of you is a big black... bear. It stares at you. You
    notice a door behind the bear. To the side of the bear you see a spear propped up against
    the wall. What do you do?"""
    print"1. Fight the bear"
    print"2. Pick up the spear"
    print"3. try to run away"    
    bear = raw_input(">")
    if (bear == "1" and spear == True) :
        print "You fight and kill the bear"
    
    elif (bear == "1" and spear == False):
        dead("the bear claws your face off")
        
    elif (bear == "2" and spear == True):
        print "You already have the spear"
        bear_room()
        
    elif (bear == "2" and spear == False):
        print "you picked up the spear"
        bear_room(spear = True)
    elif (bear == "3"):
        dead("The Bear catches you and rips your head off")
    
    else:
        print "Please choose what to do!"
        bear_room(spear)
        
        
    
    
        

bear_room(spear)