# template for "Stopwatch: The Game"
import simplegui

# define global variables
position1=[175,50]
size1=40
color1='green'
games=0
win=0

t=0
position0=[75,200]
size0=50
color0='red'

stoped=False

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    return str(t//600) + ':' + str(t%600//100) + str(t%600//10%10) + '.' + str(t%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global stoped
    timer.start()
    stoped=False
    return

def stop_handler():
    global win, games, stoped
    if stoped==False:
        timer.stop()
        stoped=True
        games+=1
        if t%10==0:
            win+=1
    return

def reset_handler():
    global t, win, games, stoped
    t=0
    win=0
    games=0
    stoped=False
    return

def draw(canvas):
    canvas.draw_text(str(win) + '/' + str(games), position1, size1, color1)
    canvas.draw_text(format(t), position0, size0, color0)
    return

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    return

# create frame
f=simplegui.create_frame ('Stopwatch: The Game', 300, 300)

# register event handlers
f.add_button('Start',start_handler, 100)
f.add_button('Stop', stop_handler, 100)
f.add_button('Reset', reset_handler, 100)
timer=simplegui.create_timer(100,timer_handler)
f.set_draw_handler(draw)

# start timer and frame
f.start()

# remember to review the grading rubric