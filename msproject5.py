#! /usr/bin/env python
from random import shuffle
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
value = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


# Show cards and its values
<<<<<<< HEAD
# The first list can be player's or dealer's, second list will always be dealer's, if there's one
def show_cards(list_cards, name, dealer_list_cards = []):
    # If it's the player's time, show the first dealer's card and its value
=======
def show_cards(list_cards, name, dealer_list_cards = []):
    # Show dealer's card if it's player's cards being showed
>>>>>>> c5189ea799de9a85e57ad51194e1b7c507b46d41
    if name == 'player':
        print('Dealer\'s cards')
        print(dealer_list_cards[0], end=', ')
        print('???????????', end=' ')
<<<<<<< HEAD
        # If the card is an ace, show the two possible values
        if dealer_list_cards[0].rank == 'Ace':
            print(dealer_list_cards[0].value, 'or', dealer_list_cards[0].value + 10)
        print(dealer_list_cards[0].value)
    # Show show player's or dealer's card
    print(f'{name} cards')
    for turn in list_cards:
        print(turn, end=', ')
        # If the card is an ace, show the two possible values and continue to next card
=======
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
>>>>>>> c5189ea799de9a85e57ad51194e1b7c507b46d41
        if turn.rank == 'Ace':
            print(turn.value, 'or', turn.value + 10)
            continue
        print(turn.value)


# def values_verification(list_cards_values, name, fvalue = 0, compare_value = 0, b_amount = 0):
#     while True:
#         if name == 'player':
#             hit_or_stand = input('Hit or Stand? ').lower()
#             if hit_or_stand == 'stand':
#                 print('Total', fvalue)
#                 return fvalue
#             list_cards_values.append(dealer.give_cards())
#             print(list_cards_values[-1], list_cards_values[-1].value)
#         value1 = value2 = 0
#         value2_validation = False
#         for value in list_cards_values:
#             if type(value.value) == type([]) and value2_validation == False:
#                 value1 += value.value[0]
#                 value2 += value.value[1]
#                 value2_validation = True
#             elif type(value.value) == type([]) and value2_validation == True:
#                 value1 += value.value[0]
#                 value2 += value.value[0]
#             else:
#                 value1 += value.value
#                 value2 += value.value
#         if name == 'player' and value2 < 21 and value2_validation == True:
#             print(f'Total {value2}')
#         elif name == 'player' and value2 > 21 or name == 'player' and value2_validation == False:
#             print(f'Total {value1}')
#         if value2 <= 21 and value2_validation == True:
#             if name == 'player':
#                 if value2 < 21:
#                     print(value1, 'or', value2)
#                     fvalue = value2
#                 elif value2 == 21:
#                     print(value2, 'BlackJack!')
#                     fvalue = value2
#                     break
#             else:
#                 if value2 < compare_value:
#                     print(value2, 'hitting')
#                     list_cards_values.append(dealer.give_cards())
#                     print(list_cards_values[-1], list_cards_values[-1].value)
#                 elif value2 > compare_value:
#                     print('Dealer wins!', value2)
#                     dealer.t_g_money(b_amount, 'increase')
#                     break
#                 elif value2 == compare_value:
#                     print('Take money back')
#                     player.receive_money(b_amount)
#                     break
#         else:
#             if value1 > 21:
#                 if name == 'dealer':
#                     print(value1, f'Bust! Player {player.name} win!')
#                     player.receive_money(dealer.t_g_money(bet_amount, 'decrease'))
#                     break
#                 else:
#                     print(value1, 'Bust!')
#                     fvalue = 0
#                     break
#             if name == 'player':
#                 if value1 < 21:
#                     fvalue = value1
#                 elif value1 == 21:
#                     print(value1, 'BlackJack!')
#                     fvalue = value1
#                     break
#             else:
#                 if value1 < compare_value:
#                     print(value1,'hitting')
#                     list_cards_values.append(dealer.give_cards())
#                     print(list_cards_values[-1], list_cards_values[-1].value)
#                 elif value1 > compare_value:
#                     print('Dealer wins!', value1 )
#                     dealer.t_g_money(b_amount, 'increase')
#                     break
#                 elif value1 == compare_value:
#                     print('Take money back')
#                     player.receive_money(b_amount)
#                     break
#     if name == 'player':
#         return fvalue


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
    name = str(input("What's your name? "))
    player = Player(name)
    dealer.shuffle_cards()
    while True:
        final_value = 0
        # Get player bet if it is a valid int number and it's within the available amount
        while True:
            bet_amount = input(f'{player} | Bet value: | Q to quit ')[0].lower()
            print(bet_amount)
            if bet_amount == 'q':
                break
            try:
                bet_amount = int(bet_amount)
            except:
                print('Enter a valid number')
                continue
            if bet_amount == 0:
                print('You don\'t have money to keep playing')
                break
            if bet_amount > player.money:
                print('You don\'t have anough money for this bet')
                continue
            player.bet(bet_amount)
            break
        dealer_cards = []
        player_cards = []
        # Loop to give dealer's and player's cards
        for turn in range(2):
            player_cards.append(dealer.give_cards())
            dealer_cards.append(dealer.give_cards())
        while True:
            show_cards(player_cards,'player', dealer_cards)
            # final_value = values_verification(player_cards, 'player', final_value)
            show_cards(dealer_cards, 'dealer')
            # values_verification(dealer_cards, 'dealer',final_value, final_value, bet_amount)
            break
        play = input('Do you want to play again? Y or N ').upper()
        if play == 'N':
            break
