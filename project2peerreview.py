# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# initialize global variables used in your code
num_range = 100

# define event handlers for control panel
def init():
    global num, rem
    num = random.randrange(0, num_range)
    rem = math.ceil(math.log(num_range, 2))
    print 'New game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', rem
    print

import random
import math

def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    init()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    init()
    
def get_input(guess):
    # main game logic goes here	
    global rem
    print 'Guess was', guess

    i = int(guess)
    if i == num:
        print 'You win!'
        print; init(); return
    
    rem -= 1
    print 'Number of remaining guesses is', rem
    
    if rem == 0:
        print 'You ran out of guesses. The number was', num
        print; init(); return

    if i < num: print 'Higher!'
    else: print 'Lower!'
    print

# create frame
import simplegui
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements
frame.add_button('Range: 0-100', range100, 100)
frame.add_button('Range: 0-1000', range1000, 100)
frame.add_input('Your guess', get_input, 100)

# start frame
init()
frame.start()
