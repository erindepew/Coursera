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
pad1_pos = [0, 60] 
pad2_pos = [600, 60]
paddle1_vel = 0 
paddle2_vel = 0 
ball_pos = [WIDTH/2, HEIGHT/2] 
ball_vel = [0, 0]
right = True 
score_left = 0 
score_right = 0 

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_vel, WIDTH, HEIGHT, ball_pos 
    if right == True:
       ball_pos = [WIDTH/2, HEIGHT/2]
       ball_vel[0] = random.randrange(1, 4)
       ball_vel[1] = random.randrange(-4, 0)  
    else: 
       ball_pos = [WIDTH/2, HEIGHT/2]
       ball_vel[0] = random.randrange(-4, -1)
       ball_vel[1] = random.randrange( -4, 0)
        

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score_left, score_right, right 
    right = not right 
    score_left = 0 
    score_right = 0 
    ball_init(right)
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global right, score_left, score_right
    # update paddle's vertical position, keep paddle on the screen
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
# draw paddles
    c.draw_polygon([(0, pad1_pos[1]), (PAD_WIDTH, pad1_pos[1]),(PAD_WIDTH, pad1_pos[1]+ PAD_HEIGHT), 
    (0, pad1_pos[1]+PAD_HEIGHT)], 12, "Blue", "Blue")   
    c.draw_polygon([(WIDTH, pad2_pos[1]), (WIDTH-PAD_WIDTH, pad2_pos[1]),
    (WIDTH-PAD_WIDTH, pad2_pos[1]+ PAD_HEIGHT), (WIDTH, pad2_pos[1]+PAD_HEIGHT)], 12, "Blue", "Blue") 
# update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0] 
    ball_pos[1] = ball_pos[1] + ball_vel[1]
# update paddles
    # error checking for paddle 1 
    if pad1_pos[1] <= 320 and pad1_pos[1] > 0: 
        pad1_pos[1] = pad1_pos[1] + paddle1_vel
    elif pad1_pos[1] > 320 and paddle1_vel < 0:   
        pad1_pos[1] = pad1_pos[1] - 5 
    elif pad1_pos[1] == 0 and paddle1_vel > 0: 
         pad1_pos[1] = pad1_pos[1] + 5 
    # error checking for paddle 2        
    if pad2_pos[1] <= 320 and pad2_pos[1] > 0: 
        pad2_pos[1] = pad2_pos[1] + paddle2_vel
    elif pad2_pos[1] > 320 and paddle2_vel < 0:   
        pad2_pos[1] = pad2_pos[1] - 5 
    elif pad2_pos[1] == 0 and paddle2_vel > 0: 
         pad2_pos[1] = pad2_pos[1] + 5 
       
#reflect ball off of paddle and check for left and right walls 
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH + 10: 
        if ball_pos[1] >= pad1_pos[1]- 10 and ball_pos[1] <= pad1_pos[1] + 90: 
            ball_vel[1] = -(ball_vel[1] + (ball_vel[1] * .1)) 
            ball_vel[0] = -(ball_vel[0] + (ball_vel[0] * .1)) 
    #respawn ball and update score_left
        else:
            score_left = score_left + 1 
            right = not right 
            ball_init(right)
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH - 10: 
        if ball_pos[1] >= pad2_pos[1]- 10 and ball_pos[1] <= pad2_pos[1] + 90: 
            ball_vel[1] = -(ball_vel[1] + (ball_vel[1] * .1))
            ball_vel[0] = -(ball_vel[0] + (ball_vel[0] * .1))
     #respawn ball and update score_right
        else: 
            score_right = score_right + 1 
            right = not right 
            ball_init(right)
        
#reflect ball off top and bottom walls     
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS: 
        ball_vel[1] = - ball_vel[1]
    
    # draw ball and scores
    c.draw_text(str(score_left), (150, 75), 36, "White")
    c.draw_text(str(score_right), (450, 75), 36, "White")
    
    c.draw_circle(ball_pos, BALL_RADIUS, 10, "White", "White") 
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel, PAD1_POS
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = paddle2_vel + 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = paddle2_vel - 5 
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = paddle1_vel + 5 
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = paddle1_vel - 5 
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0 
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()
