# implementation of card game - Memory
########not a perfect one, but I may borrow sth from it.

import simplegui
import random

COLUMNS = 4
ROWS    = 4

X_OFFSET    =  25
Y_OFFSET    =  25
FONT_SIZE   =  72
CARD_SPACE  =  20
CARD_WIDTH  =  75
CARD_HEIGHT = 100

FONT_LEFT_OFFSET = 15
FONT_TOP_OFFSET  = FONT_SIZE + (( CARD_HEIGHT - FONT_SIZE ) / 2)

CANVAS_WIDTH  = (X_OFFSET * 2) - CARD_SPACE + ((CARD_WIDTH  + CARD_SPACE) * COLUMNS)
CANVAS_HEIGHT = (Y_OFFSET * 2) - CARD_SPACE + ((CARD_HEIGHT + CARD_SPACE) * ROWS)


# helper function to initialize globals
def init():
    global deck, choices, moves
    deck = [{ "value" : i//2, "exposed" : False } for i in range(ROWS * COLUMNS)] 
    random.shuffle(deck)
    choices = [-1, -1]
    moves   = 0
    moves_label.set_text("Ready? OK!")
     
# define event handlers
def mouseclick(pos):
    global deck, choices, moves
    card = clicked_card(pos)
    if card < 0:
        return
    if deck[card]["exposed"]:
        return
    
    deck[card]["exposed"] = True
    
    if choices[0] < 0:
        choices[0] = card
    elif choices[1] < 0:
        choices[1] = card
        moves +=1
    else:
       if deck[ choices[0] ]["value"] != deck[ choices[1] ]["value"]:
            for i in choices:
                deck[i]["exposed"] = False 
       choices = [card,-1]
       
    moves_label.set_text("Moves: " + str(moves))
    
def clicked_card(pos):
    for i in range(len(deck)):
        t,l,b,r = card_limits(i)
        if (   pos[0] >= l 
           and pos[0] <= r
           and pos[1] >= t
           and pos[1] <= b):
                return i
    return -1

def card_limits(card_num):
    row = int( card_num / COLUMNS )
    col = int( card_num % COLUMNS )
        
    top    = (row * (CARD_SPACE + CARD_HEIGHT)) + Y_OFFSET
    left   = (col * (CARD_SPACE + CARD_WIDTH))  + X_OFFSET
    bottom = top  + CARD_HEIGHT
    right  = left + CARD_WIDTH
        
    return top, left, bottom, right    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck)):
        t,l,b,r = card_limits(i)
        
        card_color= "Blue"
        if deck[i]["exposed"]:
            card_color="White"
            
        canvas.draw_polygon([[l,t],[r,t],[r,b],[l,b]], 2, 'Red', card_color)

        font_x = l + FONT_LEFT_OFFSET
        font_y = t + FONT_TOP_OFFSET
        if deck[i]["exposed"]:
            canvas.draw_text(str(deck[i]["value"]), [font_x,font_y], FONT_SIZE, "Black")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Restart", init)
moves_label = frame.add_label("Ready? OK!")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric