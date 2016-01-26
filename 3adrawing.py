import simplegui

# define draw handler
def draw(canvas):
   
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    canvas.draw_line((50,180), (250,180), 40, "Red")
    canvas.draw_line((50,180), (250,180), 40, "Red")
    canvas.draw_line((55,170), (90,120), 5, "Red")
    canvas.draw_line((180,108), (180,160), 140, "Red")
    
    

# create frame
frame = simplegui.create_frame("drawing", 300, 300)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()