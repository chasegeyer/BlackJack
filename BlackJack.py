# create a black jack game
# create a deck of 52 cards
#
#     Create a deck of 52 cards
#     Shuffle the deck
#     Ask the Player for their bet
#     Make sure that the Player's bet does not exceed their available chips
#     Deal two cards to the Dealer and two cards to the Player
#     Show only one of the Dealer's cards, the other remains hidden
#     Show both of the Player's cards
#     Ask the Player if they wish to Hit, and take another card
#     If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#     If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#     Determine the winner and adjust the Player's chips accordingly
#     Ask the Player if they'd like to play again

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

# create a card class

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = [] # start with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = [] # start with empty string
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop() # pops last card (first on top of deck)
        return single_card

class Hand:

    def __init__(self):
        self.cards = [] # start with empty list
        self.value = 0 # start with 0 value till set
        self.aces = 0 # add attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        # card is being pulled from the Deck class (deck.deal)
        # will add value to self.value + the new card
        self.value = self.value + values[card.rank]

        #track aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        # checking to see if total value is higher than 21 if it is and have ace then you take 10 off and remove ace count
        # could put (and self.aces) special edge case
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet
        print(f'You won {self.bet} chips. You now have {self.total} chips')


    def lose_bet(self):
        self.total = self.total - self.bet
        print(f'You lost {self.bet} chips. You now have {self.total} chips')



def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?:"))
        except:
            print("Please put a integer in")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                print(f'you have bet {chips.bet}')
                break

def hit(deck,hand):


    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing # control up coming loop

    while True:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealers Turn!")
            playing = False
        else:
            print("Please Enter h or s only")
            continue

        break


#create 2 functions to show some of hand and one to show all of hand





def player_bust(player, dealer, chips):

    print("Player Bust!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_bust(player, dealer, chips):
    print('Dealer Bust! Player Wins!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer Wins. You Lost')
    chips.lose_bet()

def push(player, dealer):

    print("Dealer and Player Tie! Push!")


while True:

    #this is the game

    print("Welcome to Chase's Black Jack!")

    # Create a shuffle the deck action deal two cards to each player

    first_deck = Deck()
    first_deck.shuffle()


    player_hand = Hand()
    player_hand.add_card(first_deck.deal())
    player_hand.add_card(first_deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(first_deck.deal())
    dealer_hand.add_card(first_deck.deal())
    print(f'Dealers hand: {dealer_hand.cards[0]}')
    print(f'Your Hand: {player_hand.cards[0]} and {player_hand.cards[1]}')
    # set players chips at start of hand
    player_chips = Chips()
    # default value is 100
    # need to hand in (chips) to take_bet function
    take_bet(player_chips)

    while playing:
        # prompt player to hit and stand
        for x in player_hand.cards:
            print(x)
        print(player_hand.value)
        hit_or_stand(first_deck, player_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:

        while dealer_hand.value <= 17:
            hit(first_deck, dealer_hand)

        for i in dealer_hand.cards:
            print(i)
        print(dealer_hand.value)
        # if dealer ahs more than 21 he bust
        # if not both are under 21 so you test for
        # 1. dealer being higher than player
        # 2. player being higher than dealer
        # 3. A tie between Dealer and Player
        if dealer_hand.value > 21:

            dealer_bust(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:

            player_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:

            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value == player_hand.value:

            push(player_hand, dealer_hand)

    print(player_chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing")
        break