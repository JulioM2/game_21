#! /usr/bin/env python
from random import shuffle
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
value = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


# Show cards and its values
# The first list can be player's or dealer's, second list will always be dealer's, if there's one
def show_cards(list_cards, name, dealer_list_cards = []):
    # Show the first dealer's card and its value if it's the player's time
    if name == 'player':
        print('Dealer\'s cards')
        print(dealer_list_cards[0], end=', ')
        print('???????????', end=' ')
        # Show both possible values if the card is an ace
        if dealer_list_cards[0].rank == 'Ace':
            print(dealer_list_cards[0].value, 'or', dealer_list_cards[0].value + 10)
        else:
            print(dealer_list_cards[0].value)
    # Print whom cards are being showed
    print(f'{name} cards')
    # Show current cards and its values
    for turn in list_cards:
        print(turn, end=' ')
        # Show both possible values if the card is an ace and go to next one
        if turn.rank == 'Ace':
            print(turn.value, 'or', turn.value + 10)
            continue
        print(turn.value)


# Compare sumed cards values and show the winner
def values_verification(list_cards_values):    
    list_cards_values.append(dealer.give_cards())
    # Print the new card and its value
    print(list_cards_values[-1], list_cards_values[-1].value)
    # Card receive sum of cards
    cards_values_sum = 0
    # Variable show if an ace has already appeared
    ace_presence = False
    for card in list_cards_values:
        # Add plus 10 to card value if it is an ace and is the first one
        if card.rank == 'Ace' and ace_presence == False:
            cards_values_sum += card.value + 10
            ace_presence = True
            continue
        # Add normal card value
        cards_values_sum =+ card.value
    return cards_values_sum


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = value[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
    def __str__(self):
        return f'There are {len(self.all_cards)} at the deck'


# Class which all dealer's tasks
class Dealer:
    # Create a new deck and set the available amount of money
    def __init__(self):
        self.deck = Deck()
        self.amount = 1000000
    # Remove current first card in deck and return it
    def give_cards(self):
        return self.deck.all_cards.pop(0)
    # Shuffle the cards in the deck
    def shuffle_cards(self):
        shuffle(self.deck.all_cards)
    # Update the money available, adding or subtracting, according to operation 
    # And return the bet value plus itself in case of player's win
    def t_g_money(self, value1, operation):
        if operation == 'decrease':
            bet = value1 + value1
            self.amount -= value1
            return bet
        elif operation == 'increase':
            self.amount += value1

# Class which perform all player's tasks
class Player:
    # Set name and original value
    def __init__(self, name):
        self.name = name
        self.money = 6000
    # Updates money available after each bet
    def bet(self, value):    
        self.money -= value
        if self.money < 0:
            self.money = 0
    # Update money in case of win
    def receive_money(self, value):
        print(f'+  {value}')
        self.money += value
    # Return name and available money
    def __str__(self):
        return f'Player {self.name} has {self.money} available'


while True:
    deck = Deck()
    dealer = Dealer()
    # Get player's name
    name = str(input("What's your name? "))
    player = Player(name)
    dealer.shuffle_cards()
    while True:
        # Get player bet if it is a valid int number and it's within the available amount
        while True:
            bet_amount = input(f'{player} | Bet value: | Q to quit ')[0].lower()
            if bet_amount == 'q':
                break
            try:
                bet_amount = int(bet_amount)
            except:
                print('Enter a valid number')
                continue
            # If player enter zero by accident, ask if want to keep playing
            if bet_amount == 0:
                answer = input('Bet = 0. Still want to play? S or N')[0].lower()
                if answer == 'n':
                    break
                continue
            if bet_amount > player.money:
                print('You don\'t have anough money for this bet')
                continue
            player.bet(bet_amount)
            break
        # Populate dealer's and player's lists/hands
        dealer_cards, player_cards = [dealer.give_cards(), dealer.give_cards() for i in range(2)]
        show_cards(player_cards,'player', dealer_cards)
        # Vefiry if player gets blackjack with the two first cards and player_value gets 21, if it is a blackjack
        if player_cards[0].rank == 'Ace' or player_cards[1].rank == 'Ace' and sum(player_cards + 10) == 21:
            player_value = 21
        else:
            while True:
                while True:
                    hit_or_stand = input('Hit |1| or Stand |2|? ')
                    try:
                        hit_or_stand = int(hit_or_stand)
                        break
                    except:
                        print('Wrong value, please enter |1| or |2|')
                # If player choose to keep current value, break loop
                if hit_or_stand == 2:
                    ace_presence == False
                    # Variable to hold cards values if player wants to stand
                    player_value = 0
                    for card in player_cards:
                        if card.rank == 'Ace' and ace_presence == False:
                            player_value += card.value
                            ace_presence = True
                            continue
                        player_value += card.value
                    break
                else:
                    player_value = values_verification(player_cards)
                    # If the sum is 21 or above, break
                    if player_value >= 21:
                        break
        print('Total ', player_value)
        show_cards(dealer_cards, 'dealer')
        dealer_value = values_verification(dealer_cards)
        # If conditional to verify who win will be add later
        if True:
            pass
        # Break while loop if player don't have more money
        if player.money == 0:
            print('You don\'t have enough money to keep playing.')
            break
    # Select only the first character of what was inserted in upper case
    play = input('Do you want to play again? Y or N ')[0].upper()
    if play == 'N':
                break
