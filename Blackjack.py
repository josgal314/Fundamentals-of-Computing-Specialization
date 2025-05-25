# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

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
  


# We suggest modeling a hand as a list of Card objects that are stored in a field in the Hand object



#The __init__method should initialize the Hand object to have an empty list of Card objects. 


#The 
#add_card
# should append a Card object to this list of cards. 



#The 
#__str__
# should return a string representation of a Hand object in a human-readable form




# define hand class
class Hand:
    def __init__(self):
        pass	# create Hand object

    def __str__(self):
        pass	# return a string representation of a hand

    def add_card(self, card):
        pass	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
    
    
#Implement the get_value method for the 
#Hand class. You should use the provided VALUE dictionary to look up the value of a single 
#card in conjunction with the logic explained 
#in the video lecture for this project to compute the value of a hand. 
    
    
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
    
#We suggest modeling a deck of cards as list of cards. 

    
#You can generate this list using a pair of nested 
#for loops or a list comprehension.     


#Remember to use the 
#Card initializer to create your cards.



# Use 
#random.shuffle() to shuffle this deck of cards.


#Remember that the deck is randomized after shuffling, so the output of the 
#testing template should match the output in the comments in form but not in exact value.




    
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        pass	# deal a card object from the deck
    
    def __str__(self):
        pass	# return a string representing the deck


    
    
#Implement the handler for a "Deal" button that shuffles the deck and 
#deals the two cards to both the dealer and the player.    
    
    
    
    
#The event handler 
#deal for this button should shuffle the deck (stored as a global variable), 
#create new player and dealer hands (stored as global variables), and add two cards to each hand.    





#To transfer a card from the deck to a hand, you should use the 
#deal_card method of the 
#Deck class and the 
#add_card method of 
#Hand class in combination. 






#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True
    
    
    
    
    

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    
    
#Implement the handler for a "Hit" button. If the value of the hand is less 
#than or equal to 21, clicking this button adds an extra card to player's hand. 
#If the value exceeds 21 after being hit, print "You have busted".    
    
    
    
    
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
    
#Implement the handler for a "Stand" button. If the player has busted, remind the 
#player that they have busted. Otherwise, repeatedly hit the dealer until his hand 
#has value 17 or more (using a while loop). If the dealer busts, let the player know. 
#Otherwise, compare the value of the player's and dealer's hands. If the value of the 
#player's hand is less than or equal to the dealer's hand, the dealer wins. Otherwise 
#the player has won. Remember the dealer wins ties in our version.    


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()

#In our version of Blackjack, a hand is automatically dealt to the player 
#and dealer when the program starts. In particular, the program template 
#includes a call to the deal()function during initialization. 

frame.start()


# remember to review the gradic rubric
