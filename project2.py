# Define global variables (program state)

max_guess_times = 7
guess_times = 1
random_num = -1
# helper function for initial game

def init():
   global random_num
   global max_guess_times
   random_num = random.randrange(0, 100)
   max_guess_times = 7
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global random_num     
    global max_guess_times
    global guess_times
    random_num = random.randrange(0, 100)
    max_guess_times = 7
    guess_times = 1
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global random_num 
    global max_guess_times
    global guess_times
    random_num = random.randrange (0, 1000)
    max_guess_times = 10
    guess_times = 1
    

def get_input(guess):
    # main game logic goes here	
    global guess_times
    print "guess_times: " + str(guess_times)
    if guess_times < max_guess_times:
       print "you have: " + str (max_guess_times-guess_times) + " guesses left!"
       guess_times = guess_times + 1
      
    elif guess_times == max_guess_times:
       guess_times = guess_times + 1
       print "max guess times reached!"
    else:
       print "error, you have exceeded max times of guess!"
       return
    guess_num = int (guess)
    if guess_num > random_num:
       print "guess is higher"
    elif guess_num < random_num:
       print "guess is lower"
    else:
       print "guess number equals computer number"
        
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

