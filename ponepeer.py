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
right = random.choice([True, False])
paddle1_vel=paddle2_vel = [0,0]
ball_vel =[5,-5]
paddle2_vel= [0,0]
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2] 
paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT/2]
restart_status = 0
score1 = score2 =0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel,righ # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if right == True:
        ball_dir = 1
    else: ball_dir = -1       
    ball_vel[0] = ball_dir*random.randrange(2, 4)
    ball_vel[1] = -random.randrange(1, 3) 
    
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,right, restart_status,score1, score2  # these are floats
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2] 
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT/2]
    global score1, score2  # these are ints
    score1 = score2 = 0   
    if restart_status :
        ball_init(right)
    
def restart():
    global restart_status
    restart_status =1
    init()
        
def up_date():
    global paddle1_pos, paddle2_pos, paddle1_vel,  paddle2_vel
    if paddle1_vel[1] < 0:   
        if (paddle1_pos[1] + paddle1_vel[1] - HALF_PAD_HEIGHT) <= 0:
            paddle1_vel[1] = 0
            paddle1_pos[1] = HALF_PAD_HEIGHT
    if paddle2_vel[1] < 0:   
        if (paddle2_pos[1] + paddle2_vel[1] - HALF_PAD_HEIGHT) <= 0:
            paddle2_vel[1] = 0
            paddle2_pos[1] = HALF_PAD_HEIGHT
    if paddle1_vel[1] > 0:   
        if (paddle1_pos[1] + paddle1_vel[1] + HALF_PAD_HEIGHT - HEIGHT) >= 0:
            paddle1_vel[1] = 0
            paddle1_pos[1] = HEIGHT-HALF_PAD_HEIGHT
    if paddle2_vel[1] > 0:   
        if (paddle2_pos[1] + paddle2_vel[1] + HALF_PAD_HEIGHT - HEIGHT) >= 0:
            paddle2_vel[1] = 0
            paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT         
            
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, restart_status
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles 
    c.draw_polygon([[0, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [0, paddle1_pos[1] + HALF_PAD_HEIGHT]], 1, "Red", "White")
    c.draw_polygon([[WIDTH -1 - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], 1, "Red", "White")
    
    # draw ball and score
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    c.draw_text(str(score1), (150, 50), 24,"Blue")
    c.draw_text(str(score2), (450, 50), 24,"Blue")
        
    if restart_status:
    # update paddle's vertical position, keep paddle on the screen
        up_date()
        paddle1_pos[0] += paddle1_vel[0]
        paddle1_pos[1] += paddle1_vel[1]
        paddle2_pos[0] += paddle2_vel[0]
        paddle2_pos[1] += paddle2_vel[1]

    # update ball
        if (BALL_RADIUS >= ball_pos[1]) or (ball_pos[1]>= (HEIGHT- BALL_RADIUS)):
            ball_vel[1] = - ball_vel[1]
        elif (PAD_WIDTH +BALL_RADIUS >= ball_pos[0]):        
            if not ((paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1]) and (ball_pos[1] <= (paddle1_pos[1] + HALF_PAD_HEIGHT))):
                score2 +=1
                right = True
                ball_init(right)
#                ball_vel[0] = - ball_vel[0]
            else:	ball_vel[0] = - 1.1*ball_vel[0]
        elif (WIDTH -PAD_WIDTH- BALL_RADIUS) <= ball_pos[0]:      
            if not ((paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1]) and (ball_pos[1] <= (paddle2_pos[1] + HALF_PAD_HEIGHT))):
                score1 +=1
                right = False
                ball_init(right)
#                ball_vel[0] = - ball_vel[0]            
            else:	ball_vel[0] = - 1.1*ball_vel[0]
            
    # Update ball position
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]            
            
def keydown(key):
    global paddle1_vel, paddle2_vel    
    acc =5
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["down"]:
      paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
     paddle2_vel[1] -= acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
       paddle1_vel[1]= 0
    elif key==simplegui.KEY_MAP["down"] or key==simplegui.KEY_MAP["up"]:
      paddle2_vel[1] = 0
 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

# start frame
frame.start()
