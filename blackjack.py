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
outcome = ""
score = 0
message = "Hit or stand?"


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
        
# define hand class
class Hand:
    def __init__(self):
        self.cardsOnHand = list()
        #pass	# replace with your code

    def __str__(self):
        for card in self.cardsOnHand:
            print card
        pass	# replace with your code

    def add_card(self, card):
        self.cardsOnHand.append(card)
        pass	# replace with your code

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        Hand_value = 0
        doesContainAces = False
       #to walk through every card in the list to see if there is Aces and also calculate the
       # total value of the cards.
        for card in self.cardsOnHand:
            Hand_value += VALUES[card.rank]
            if card.rank == 'A':
                doesContainAces = True
        if (not doesContainAces):
            return Hand_value
        else:
            if Hand_value + 10 <= 21:  #count in when Aces = 11.
                return Hand_value + 10
            else:
                return Hand_value
                   
        pass	# replace with your code

    def busted(self):
        if self.get_value() > 21:
           return True
        else:
           return False
               
           
    def draw(self, canvas, p):
        position = p
        for card in self.cardsOnHand:
           card.draw(canvas, position)
           position[0] = position[0] + 90
                   
        pass	# replace with your code
 
        
# define deck class
class Deck:
    def __init__(self):
        self.cardsInDeck = list()
        for suit in SUITS:
            for rank in RANKS:
                self.cardsInDeck.append(Card(suit, rank))#Card(suit, rank) is to construct an object of Card.
        
        pass	# replace with your code

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cardsInDeck)        
        pass	# replace with your code

    def deal_card(self):
        return self.cardsInDeck.pop(0) #remove one card from the top
        
        pass	# replace with your code


#define event handlers for buttons
player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
    
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, message
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand =Hand()
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    outcome = ""
    message = "Hit or stand?"
    # your code goes here
    
    in_play = True

def hit():
    global outcome, in_play, player_hand, score, deck, message
    #print in_play
    if (in_play):
        #print in_play
        player_hand.add_card(deck.deal_card())
        if (player_hand.busted()):
            outcome = "You went to bust and lose!"
            in_play = False
            score = score - 1;
            message = "New deal?"
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global dealer_hand, deck, player_hand, in_play, score, outcome, message
    if in_play:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck.deal_card())
        if (dealer_hand.busted()):
            outcome = "You win!"
            score += 1
        else:
            if (dealer_hand.get_value() > player_hand.get_value()):
                outcome = "You lose!"
                score -= 1
            elif (dealer_hand.get_value() == player_hand.get_value()):
                outcome = "Tie!"
            else:
                outcome = "You win!"
                score += 1
        in_play = False
        message = "New deal?"
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
       
    player_hand.draw(canvas, [80, 400])
    
    dealer_hand.draw(canvas, [80, 200])
   
    if in_play:
         canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [80 + 0.5*CARD_SIZE[0], 200 + 0.5*CARD_SIZE[1]], CARD_BACK_SIZE)
    #
    #card = Card("S", "A")
    #card.draw(canvas, [80, 400])
    #card = Card("S", "A")
    #card.draw(canvas, [170, 400])
    #card = Card("S", "A")
    #card.draw(canvas, [260, 400])
    
    #card = Card("S", "A")
    #card.draw(canvas, [80, 200])
    #card = Card("S", "A")
    #card.draw(canvas, [170, 200])
    #card = Card("S", "A")
    #card.draw(canvas, [260, 200])
    
    canvas.draw_text("Blackjack", [100,100], 40, "Fuchsia")
    canvas.draw_text("Score", [380,100], 25, "white")
    canvas.draw_text(str(score), [475,100], 25, "white")
    canvas.draw_text("Player", [80,368], 25, "yellow")
    canvas.draw_text(message, [200,368], 25, "white")
    canvas.draw_text("Dealer", [80,170], 25, "yellow")
    canvas.draw_text(outcome, [200,170], 25, "white")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()
deal()

# remember to review the gradic rubric
# http://www.codeskulptor.org/#user5-SlbzuQ8PCm-1.py