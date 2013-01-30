# "Stopwatch: The Game"
import simplegui

# Global variables: time, interval, time print-out
# scores, tries, and error checking

time_seconds = 0 
timer_interval = 100
current_time = ''
counter_score = 0 
counter_try = 0 
score = '0/0'
time_stop = False

def format(t):
   ''' (int) -> (str) 
	Takes time in tenths of a second and converts it into 
	the formatted string A:BC.D
	''' 
   tenth_seconds = t%10 
   seconds1 = ((t%100)- tenth_seconds)/ 10
   minutes = (t//600)
   seconds2 = ((t//100)- (minutes * 6))
   return str(minutes)+ ':' + str(seconds2) + str(seconds1)+ '.' + str(tenth_seconds)

# Starts timer and resets error checking to False.
def timer_start():
    global time_stop
    timer.start()
    time_stop = False

# Stops timer. If stops on whole second, +1 score.
# Updates canvas score.	
def timer_stop():
    global time_seconds, counter_score, counter_try, score, time_stop
    timer.stop()
    if time_seconds%10 == 0 and time_stop == False:  
        counter_score = counter_score + 1
        counter_try = counter_try + 1
        time_stop = True
    elif time_seconds%10 != 0 and time_stop == False: 
        counter_try = counter_try + 1 
        time_stop = True 
    score = str(counter_score) + '/' + str(counter_try) 

# Reset timer. Set all global variables to original values.
def timer_reset(): 
    global time_seconds, score, time_stop, current_time, counter_score, counter_try
    current_time = '0:00.0'
    time_seconds = 0 
    score = '0/0'
    time_stop = False
    timer.stop()
    counter_score = 0 
    counter_try = 0 
       
def timer(): 
    ''' 
	(null) -> (str) 
	Event handler for timer. Increments time_seconds by 
	1 every tenth of a second.
	''' 
    global time_seconds, current_time
    time_seconds = time_seconds + 1
    current_time = format((time_seconds))
    return current_time 

# Draws on canvas. 
def draw(canvas): 
    canvas.draw_text(current_time, [100, 150], 30, "White")
    canvas.draw_text(score, [30, 30], 30, "White") 
    
# Create frame. 
frame = simplegui.create_frame("Timer", 300, 300)

# Create timer. 
timer = simplegui.create_timer(timer_interval, timer)

# Event Handlers
frame.set_draw_handler(draw)
frame.add_button("Start", timer_start, 60)
frame.add_button("Stop", timer_stop, 60)
frame.add_button("Reset", timer_reset, 60) 

# Start timer and frame. 
timer.start()
frame.start()