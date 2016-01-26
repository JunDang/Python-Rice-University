# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-1,  1] # pixels per tick
time = 0


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_vel = [-1,  1]
   
  
    
    

    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [PAD_WIDTH / 2, PAD_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, PAD_HEIGHT]
    print paddle2_pos
    paddle1_vel = [1]
    paddle2_vel = [1]
    
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    
    c.draw_polygon([(paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1]- HALF_PAD_HEIGHT ) 
                    ,(paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT ) 
                    ,(paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT)
                    ,(paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] - HALF_PAD_HEIGHT)], 2, "red", "White")
    
       # c.draw_polygon([(paddle2_pos[0] - PAD_WIDTH / 2 , paddle2_pos[1]-PAD_HEIGHT / 2 ) 
        #            ,(paddle2_pos[0] - PAD_WIDTH / 2 , paddle2_pos[1] + PAD_HEIGHT / 2 ) 
         #           ,(paddle2_pos[0] + PAD_WIDTH / 2 , paddle2_pos[1] + PAD_HEIGHT / 2)
           #         ,(paddle2_pos[0] + PAD_WIDTH / 2 , paddle2_pos[1] - PAD_HEIGHT / 2)], 2, "red", "White")
    #
    
     
    # update ball
     # create a list to hold ball position
    #ball_pos = [0, 0]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH or  ball_pos[0] >= WIDTH - PAD_WIDTH -1 - BALL_RADIUS:
         ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-1-BALL_RADIUS:
         ball_vel[1] = - ball_vel[1]
     
   

 
  
   
            
    # draw ball and scores
    # create a list to hold ball position
    #ball_pos = [WIDTH / 2, HEIGHT / 2]
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "white", "White")
    #print ball_pos
  
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
           #paddle1_vel = 1 
           #paddle2_vel = 1
           #if key == simplegui.KEY_MAP["down"]:
           #paddle1_pos[1] += vel
           #elif key == simplegui.KEY_MAP["w"]:
           #paddle2_pos[1] += vel        
    
        
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
           #paddle1_vel = float(2) , paddle2_vel = float(2)
          # if key == simplegui.KEY_MAP["up"]:
           #paddle1_pos[1] -= vel
           #elif key == simplegui.KEY_MAP["s"]:
           #paddle2_pos[1] -= vel
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()