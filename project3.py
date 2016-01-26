# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
current = 0
play_time = 0
success_time = 0
isStopped = True
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    A = int(t/600)
    E = t%600
    B = int(E/100)
    C = int(E/10)%10
    D = E%10

    return str(A) + ":" + str(B)+ str(C) + "." + str(D)
    
             
       
  
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global isStopped
    isStopped = False
    timer.start ()
    
def stop_handler():
    global play_time
    global success_time
    global isStopped
   
    if (not isStopped):     
       timer.stop ()
       isStopped = True
       play_time += 1
       #print play_time
       E = current%600
       C = int(E/10)%10
       D = E%10
       if D == 0:
          success_time += 1
       else:
          success_time += 0
    
    
    
def reset_handler():
    global current
    global play_time
    global success_time
    timer.stop()
    current = 0
    play_time = 0
    success_time = 0
    



# define event handler for timer with 0.1 sec interval
def timer_handler():
    global current
    current += 1
    
def draw(canvas):
    """Draw message."""
    canvas.draw_text(format(current), [90,115], 36, "Red")
    canvas.draw_text(str(success_time)+ "/" + str (play_time), [250,30], 20, "Green")
    
# create frame
f = simplegui.create_frame("stopwatch", 300, 200)

# register event handlers
f.add_button("start", start_handler, 200)
f.add_button ("stop", stop_handler, 200)
f.add_button("reset", reset_handler, 200)
timer = simplegui.create_timer(interval, timer_handler)


# start timer and frame
f.set_draw_handler(draw)

# Start the frame animation

f.start()

http://www.codeskulptor.org/#user4-nfz7lU1qem-1.py

