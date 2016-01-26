implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def init():
    global numbers
    global exposed
    numbers = range(16)
    for i in numbers:
        numbers [i] = numbers [i]%8
    random.shuffle(numbers)
    exposed = range (16)
    for i in exposed:
        exposed [i] = True
    #exposed[6] = False
    #print exposed
    global state
    state = 0
    global moves
    moves = 0
	l.set_text("Moves = 0")
    pass  

     
# define event handlers
def mouseclick(pos):
    atleastOneisTrue = False
    for i in exposed:
        if (i):
            atleastOneisTrue = True
            break
    if (not atleastOneisTrue):
        return
    exposed [pos[0]//50] = False  
    global state, moves
    global firstOpenedCard
    global secondOpenedCard
    if state == 0:
        firstOpenedCard = pos[0]//50
        moves += 1
        l.set_text("Moves = " + str(moves))
        state = 1
    elif state == 1:
        secondOpenedCard = pos[0]//50
        state = 2
    else:
        if (numbers[firstOpenedCard] == numbers[secondOpenedCard]): 
            exposed[firstOpenedCard] = False
            exposed[secondOpenedCard] = False
        else:
            exposed[firstOpenedCard] = True
            exposed[secondOpenedCard] = True
        firstOpenedCard = pos[0]//50   #第三张牌变为下一轮的第一张牌
        moves += 1
        l.set_text("Moves = " + str(moves))
        state = 1        
    pass

    
def getCard(i):
    return [(50 *(i-1), 0), (50 *(i-1), 100), (50 *i, 100),(50*i, 0) ]

def getNumbers(i):
    return (50 *(i-1), 80)

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_text(str(numbers[i]), getNumbers(i+1), 60, "Red")
        if (exposed[i]):
           canvas.draw_polygon(getCard(i+1), 1, "Black", "Green")  
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
#http://www.codeskulptor.org/#user5-qFvh7irzog-15.py