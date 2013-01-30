# Card game - Memory

import simplegui
import random

mem_deck = [] 
exposed = []
state = []
text = 0 

# Initialize globals
def init():
    global mem_deck, new_deck, exposed, text
    mem_deck = []
    exposed = []
    state = []
    text = 0 
    for i in range(0, 8):
        mem_deck.append(i) 
        mem_deck.append(i)
        
    for i in range(0, 16):  
        exposed.append(False) 
        
    random.shuffle(mem_deck)     
    
# Mouse click event handler
def mouseclick(pos):
    global mem_deck, state, text
    index = pos[0]//50 
    value = mem_deck[index]
    card = [index, value] 
     
    if len(state)== 0 and exposed[index] != True: 
        exposed[index] = True
        state.append(card)
        text = text + 1 
  
    elif len(state) == 1 and exposed[index] != True:
        exposed[index] = True
        state.append(card)
        text = text + 1 
        
    elif len(state) == 2 and exposed[index] != True: 
         exposed[index] = True
         state.append(card)
         card1 = state[0] 
         card2 = state[1] 
         text = text + 1 
# Determine if exposed cards are matching
         if card1[1] == card2[1]:
            state.remove(card1) 
            state.remove(card2)
         elif card1[1] != card2[1]:
            state.remove(card1) 
            state.remove(card2) 
            exposed[card1[0]] = False 
            exposed[card2[0]] = False
                                                       
def draw(canvas):
    global mem_deck, exposed, text
    x_point = 25
# Draw exposed cards 
    for i in range (len(exposed)):
        if exposed[i] == True:
            canvas.draw_text( str(mem_deck[i]) , (x_point, 50), 12, "White")
            x_point = x_point + 50 
        elif exposed[i] == False: 
            canvas.draw_polygon([(x_point+24 , 0), (x_point-24, 0), (x_point-24, 100), (x_point+24, 100)], 1, "Green", "Green")
            x_point = x_point + 50 
            
    l.set_text("Moves = " + str(text))
     
# Create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# Initialize global variables
init()

# Register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()