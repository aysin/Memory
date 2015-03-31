# implementation of card game - Memory

import simplegui
import random

firstClick = 0
secondClick = 0

# helper function to initialize globals
def new_game():
    global exposed, cardlist, turn, state
    turn = 0
    state = 0
    cardlist = [a%8 for a in range(16)]  
    exposed = [False for a in range(16)]
    
    random.shuffle(cardlist)
    label.set_text("Turns = " + str(turn))
    pass
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, cardlist, turn, state, firstClick, secondClick
    choice = int(pos[0] / 50)
    if state == 0:
        state = 1
        firstClick = choice
        exposed[firstClick] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            secondClick = choice
            exposed[secondClick] = True
            turn += 1
    elif state == 2:
        if not exposed[choice]:
            if cardlist[firstClick] == cardlist[secondClick]:
                pass
            else:
                exposed[firstClick] = False
                exposed[secondClick] = False
                
            firstClick = choice
            exposed[firstClick] = True
            state = 1
    label.set_text("Turns = " + str(turn))
    pass
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for a in range(16):
        if exposed[a]:
            canvas.draw_text(str(cardlist[a]), (50*a + 10, 60), 50, "White")
        else:
            canvas.draw_polyline([(50*a, 0), (50*a, 100), (50*a + 50, 0), (50*a + 50, 100)], 5, "Blue")
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game, 150)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
