# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
game_state = 0
score = [0, 0]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        
    def __str__(self):
        self.hand = [card for card in self.hand]
        return str(self.hand) 

    def add_card(self, card):
        self.hand.append(card) 

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        i = 0 
        hand_sum = 0 
        ace_true = False
        while i < len(self.hand):
            card = self.hand[i]
            dic_key = card[1]
            hand_sum = hand_sum + VALUES.get(dic_key)
         
            if 'A' in [card[1] for card in self.hand]: 
                ace_true = True           
            i += 1 
                
        if hand_sum <= 11 and ace_true == True: 
            hand_sum = hand_sum + 10 
            return hand_sum 
        else: 
            return hand_sum 

    def busted(self):
        busted = False 
        value = self.get_value()
        if value > 21: 
            busted = True
            return busted 
        else: 
            return busted 
    
    def draw(self, canvas, p): 
        pos = p
        for i,j in self.hand:
            card = Card(i,j)
            card.draw(canvas, pos) 
            pos[0] += 20                
 
# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            cards_of_suit = zip([suit for i in range(1, 14)], [card for card in RANKS])
            for tpl in cards_of_suit:
                self.deck.append(tpl) 
        
    # add cards back to deck and shuffle
    def shuffle(self):
        global SUITS, RANKS
        random.shuffle(self.deck) 
        return self.deck

    def deal_card(self):
        pop_card= self.deck.pop(0)
        return pop_card 
    
    def __str__(self):
        return Deck	


#define event handlers for buttons
def deal():
    global in_play, game_state, score
        
    Deck.__init__()
    player_hand.__init__()
    dealer_hand.__init__()
    Deck.shuffle()
        
    in_play = False
    game_state = 0
        
    i = 0  
    j = 0 
    Deck.shuffle()
    while i < 2: 
        cur_card = Deck.deal_card() 
        dealer_hand.add_card(cur_card)
        i += 1 
    while j < 2: 
        cur_card = Deck.deal_card() 
        player_hand.add_card(cur_card) 
        j += 1
    
    in_play = True

def hit():
    global in_play, game_state, score
    
    if in_play: 
        player_hand.add_card(Deck.deal_card()) 
        if player_hand.get_value() > 21:
            score[1] += 1
            in_play = False
            game_state = 1 # Player Busted   
                 
def stand():
    global in_play, game_state, score
    
    if in_play:
        d_hand = dealer_hand.get_value()
        if d_hand < 18:
            dealer_hand.add_card(Deck.deal_card())
            stand()
        elif d_hand > 21:
            score[0] += 1
            game_state = 2 # Dealer Busted
            in_play = False
        elif d_hand < player_hand.get_value():
            score[0] += 1
            game_state = 3 # Player Wins
            in_play = False
        else:
            score[1] += 1
            game_state = 4 # Dealer Wins
            in_play = False

# draw handler    
def draw(canvas):
    global in_play, game_state
    p_player = [100, 300]
    p_dealer = [100, 100] 
    # Hands
    player_hand.draw(canvas, p_player)
    dealer_hand.draw(canvas, p_dealer)
    canvas.draw_text("Dealer: " + str(score[1]) + " Player: " + str(score[0]), [50, 50],  32, "White") 
    if game_state > 0: 
        if game_state == 1: 
            canvas.draw_text("You're busted! Dealer wins!", [100,500], 32, "White")
        elif game_state == 2: 
            canvas.draw_text("Dealer busted! You win!", [100,500], 32, "White")
        elif game_state == 3: 
            canvas.draw_text("You win!", [100,500], 32, "White") 
        elif game_state == 4:
            canvas.draw_text("Dealer wins!", [100,500], 32, "White")      

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

Deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
Deck.shuffle()
    
frame.start()
