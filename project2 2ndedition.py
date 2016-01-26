# SimpleGUI program template

# Import the module
import simplegui
import random
import math

# Define global variables (program state)

max_guess_times = 7
guess_times = 0
random_num = -1
# helper function for initial game

def init():
   global random_num
   global max_guess_times
   random_num = random.randrange(0, 100)
   max_guess_times = 7
   print "New game. Range is from 0 to 100"
   print "Number of remaining guessess is:" + str(max_guess_times - guess_times)
   print " "
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global random_num     
    global max_guess_times
    global guess_times
    random_num = random.randrange(0, 100)
    max_guess_times = 7
    guess_times = 0
    print "New game. Range is from 0 to 100"
    print "Number of remaining guessess is:" + str(max_guess_times - guess_times)
    print " "
    
   
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global random_num 
    global max_guess_times
    global guess_times
    random_num = random.randrange (0, 1000)
    max_guess_times = 10
    guess_times = 0
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guessess is:" + str(max_guess_times - guess_times)
    print " " 
    

def get_input(guess):
    # main game logic goes here	
    global guess_times
    guess_num = int (guess)
    print "Guess was: " + str(guess_num)
    guess_times = guess_times + 1
    if guess_times == max_guess_times:
       print "Number of remaining guessess is 0"
       print "You ran out of games! the number was:" + str(random_num)
       return
    elif guess_times < max_guess_times:        
       print "Number of remaining guesses is " + str (max_guess_times-guess_times)  
       
    else:
       return
   
    if guess_num > random_num:
       print "Higher!"
    elif guess_num < random_num:
       print "Lower!"
    else:
       print "Equal!"
        
    print ""
    

# Create a frame
f = simplegui.create_frame("guess the number", 200, 200)

# register event handlers for control elements

f.add_button("Range is [0, 100)", range100, 200)
f.add_button ("Range is [0, 1000)", range1000, 200)
f.add_input ('Enter a guess', get_input, 200)
 
init()
# Start frame 

f.start()
