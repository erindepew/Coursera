#Guess the number game. Player plays against a computer, guess the randomly generated number. 
import simplegui
import math
import random

#event handlers

high = 100 

def init():
    ''' initialize global variables''' 
    global secret_number, count
    secret_number = random.randrange(0,high)
    count = 7 

def check_guess(guess, secret_number):
    ''' int, int -> Null 
    Compares the user input guess with the computer generated secret_number
    Returns a printed statement of either Higher, Lower or Correct
    Also returns an error statement and re-initalizes globals
    '''
    if int(guess) > secret_number and count > 0: 
        print "Lower!" 
    elif int(guess) < secret_number and count > 0:
        print "Higher!"
    elif int(guess) == secret_number and count > 0:  
        print "Correct!"
        print "New game. Range is from 0 to " + str(high)
        init()
        frame.start()
    else: 
        print "You are out of guesses. Try again."
        print "New game. Range is from 0 to " + str(high)
        init()
        frame.start()
def range100():
    ''' Null -> int 
    Assigns to global count and high variable. 
    Generates secret_number randomly within the defined range [0,100). 
    ''' 
    global high 
    global secret_number
    global count 
    count = 7 
    high = 100
    secret_number = random.randrange(0,high) 
    print "New game. Range is from 0 to " + str(high)
    return secret_number

def range1000(): 
    ''' Null -> int 
    Assigns to global count and high variable. 
    Generates secret_number randomly within the defined range [0,1000). 
    ''' 
    global high 
    global secret_number 
    global count 
    count = 10
    high = 1000 
    secret_number = random.randrange(0,high) 
    print "New game. Range is from 0 to " + str(high)
    return secret_number  
    
def get_input(guess):
    ''' int -> int, int 
    Decrements global count. 
    Prints the value of the guess and number of guesses remaining. 
    Returns function check_guess. 
    ''' 
    global count
    count = count - 1
    print "Guess was " + str(guess)
    print "Number of remaining guesses is " + str(count) 
    return check_guess(guess, secret_number)

#buttons and input field    
frame = simplegui.create_frame("Guess the Number", 300, 200)
frame.add_button("0 - 100", range100)
frame.add_button("0-1000", range1000) 
frame.add_input("Guess", get_input, 200)

#start frame and initialize game
init()
frame.start()
