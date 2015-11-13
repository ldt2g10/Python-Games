# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 19:51:18 2015

@author: Luke
"""

print "Welcome to Luke's Game!"
print"----------------------------------------------------------------"

print""" You wake up in a dark room. You rub your head in a lot of pain
    you look around, you see no doors. Just a small window that is 
    cracked open slightly. What do you do?"""

print"1. open and look in backpack."
print"2. Try and open the Window."
    
action1 = raw_input(">")

if action1 == "1":
    print """You walk up to and open the backpack. Inside you find a bottle with
    what looks like a bottle of water and a box of what appear to be 
    biscuits. You suddenly notice how hungry and thirsty you are."""
    print"1. Drink the water."
    print"2. Eat the biscuits."
    action2 = raw_input(">")
    if action2 == "1":
        print "You drink the water. It is poison. You die very quickly."
    elif action2 == "2":
        print """You eat the biscuits. They make you very thirsty so you
        decide to drink the water. It is poison. You die."""
    else:
        print"""While debating what to do, you did not notice the 
        guard creep up behind you. He smashed your face in with an axe.
        You are dead."""
        
elif action1 == "2":
    print"""While trying to open the window a wild animal notices you.
    unequipped with anything to fight it off. It mauls you to death."""
    
else: 
    print"""You did not choose to do anything. You stand there until 
    you die of old age."""
    
 