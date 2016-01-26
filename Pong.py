# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0] # pixels per tick

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right:
       ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    else:
       ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(True)
    score1 = 0
    score2 = 0
    paddle1_pos = [PAD_WIDTH / 2, PAD_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, PAD_HEIGHT]
    #print paddle2_pos
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    new_paddle1_pos = paddle1_pos[1] + paddle1_vel[1]
    if (new_paddle1_pos >= HALF_PAD_HEIGHT) and (new_paddle1_pos <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos[1] = new_paddle1_pos
    new_paddle2_pos = paddle2_pos[1] + paddle2_vel[1]
    if (new_paddle2_pos >= HALF_PAD_HEIGHT) and (new_paddle2_pos <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos[1] = new_paddle2_pos
        
    # draw mid line and gutters
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    
    c.draw_polygon([(paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1]- HALF_PAD_HEIGHT ) 
                    ,(paddle1_pos[0] - HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT ) 
                    ,(paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] + HALF_PAD_HEIGHT)
                    ,(paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] - HALF_PAD_HEIGHT)], 2, "red", "red")
    
    c.draw_polygon([(paddle2_pos[0] - PAD_WIDTH / 2 , paddle2_pos[1]-PAD_HEIGHT / 2 ) 
                  ,(paddle2_pos[0] - PAD_WIDTH / 2 , paddle2_pos[1] + PAD_HEIGHT / 2 ) 
                  ,(paddle2_pos[0] + PAD_WIDTH / 2 , paddle2_pos[1] + PAD_HEIGHT / 2)
                  ,(paddle2_pos[0] + PAD_WIDTH / 2 , paddle2_pos[1] - PAD_HEIGHT / 2)], 2, "blue", "blue")
     
    # update ball
    # draw ball and scores
     
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "white", "White")
    c.draw_text(str(score1), [WIDTH*3/8,HEIGHT/4], 30, "red")
    c.draw_text(str(score2), [WIDTH*4.7/8,HEIGHT/4], 30, "blue")
  
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # collide and reflect off of left hand side of canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-1-BALL_RADIUS:
         ball_vel[1] = - ball_vel[1]
     
    if (ball_pos[0]-PAD_WIDTH)<= BALL_RADIUS:
       if (ball_pos[1] < paddle1_pos[1]- HALF_PAD_HEIGHT) or (ball_pos[1] > paddle1_pos[1]+ HALF_PAD_HEIGHT):
          score2 += 1
          ball_init(True)
       else:
          ball_vel[0] = - ball_vel[0] * 1.1
          ball_vel[1] = ball_vel[1] * 1.1
                
    if (ball_pos[0] + PAD_WIDTH + BALL_RADIUS + 1)>= WIDTH:
       if (ball_pos[1] < paddle2_pos[1]- HALF_PAD_HEIGHT) or (ball_pos[1] > paddle2_pos[1]+ HALF_PAD_HEIGHT):
          score1 += 1
          ball_init(False)
       else:
          ball_vel[0] = - ball_vel[0] * 1.1
          ball_vel[1] = ball_vel[1] * 1.1
                
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["s"]:
       paddle1_vel = [0, 3]
    elif key == simplegui.KEY_MAP["w"]:
       paddle1_vel = [0, -3] 
    if key == simplegui.KEY_MAP["down"]:
       paddle2_vel = [0, 3]
    elif key == simplegui.KEY_MAP["up"]:
       paddle2_vel = [0, -3]
     
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
          
    if key == simplegui.KEY_MAP["s"]:
       paddle1_vel = [0, 0]
    elif key == simplegui.KEY_MAP["w"]:
       paddle1_vel = [0, 0] 
    if key == simplegui.KEY_MAP["down"]:
       paddle2_vel = [0, 0]
    elif key == simplegui.KEY_MAP["up"]:
       paddle2_vel = [0, 0]
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
ball_init(True)
init()
frame.start()
http://www.codeskulptor.org/#user4-brxbp4yQ0w-6.py
