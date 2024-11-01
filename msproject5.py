#! /usr/bin/env python
from random import shuffle
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
value = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


# Show cards and its values
# The first list can be player's or dealer's, second list will always be dealer's, if there's one
def show_cards(list_cards, name, dealer_list_cards = []):
    # Show the first dealer's card and its value if it's the player's time
    if name == 'Player':
        print('----------Dealer\'s cards----------')
        print(dealer_list_cards[0], end=', ')
        print('???????????', end=' ')
        # Show both possible values if the card is an ace
        if dealer_list_cards[0].rank == 'Ace':
            print(dealer_list_cards[0].value, 'or', dealer_list_cards[0].value + 10)
        else:
            print(dealer_list_cards[0].value)
    # Print whom cards are being showed
    print(f'----------{name} cards----------')
    # Show current cards and its values
    for turn in list_cards:
        print(turn, end=' ')
        # Show both possible values if the card is an ace and go to next one
        if turn.rank == 'Ace':
            print(turn.value, 'or', turn.value + 10)
            continue
        print(turn.value)

# Sum cards values and compare its values
def sum_values(list_cards):
    # Variable to hold ace presence in list of cards
    ace_presence = False
    cards_values_sum = 0
    for card in list_cards:
        # Add plus 10 to card value if it is an ace and is the first one
        if card.rank == 'Ace' and ace_presence == False:
            cards_values_sum += card.value + 10
            ace_presence = True
            continue
        # Add normal card value
        cards_values_sum += card.value
    # Verify if the sum with ace's bigger value is greater than 21 and return the sum - 10 if it is
    if ace_presence and cards_values_sum > 21:
        return cards_values_sum - 10
    return cards_values_sum
    
# Add cards if hit was chosen
def hitting(list_cards_values):
    list_cards_values.append(dealer.give_cards())
    # Print the new card and its value
    print('Hitting')
    print(list_cards_values[-1], list_cards_values[-1].value)
    print('Total', sum_values(list_cards_values))
    return sum_values(list_cards_values)


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


# Class with all dealer's tasks
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
        if operation == 'give':
            bet = value1 + value1
            self.amount -= value1
            return bet
        else:
            self.amount += value1


# Class which perform all player's tasks
class Player:
    # Set name and original value
    def __init__(self, name):
        self.name = name
        self.money = 6000
    # Update money available after each bet
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
    dealer = Dealer()
    # Get player's name
    name = str(input("What's your name? "))
    player = Player(name)
    dealer.shuffle_cards()
    while True:
        # Get player bet if it is a valid int number and it's within the available amount
        while True:
            bet_amount = input(f'{player} | Bet value: | Q to quit ').upper()
            if bet_amount[0] == 'Q':
                break
            try:
                bet_amount = int(bet_amount)
                break
            except ValueError:
                print('Enter a valid number')
        # If player enter zero by accident, ask if wants to keep playing
        if bet_amount == 0:
            answer = input('Bet = 0. Still want to play? S or N')[0].upper()
            if answer == 'N':
                break
            continue
        if bet_amount > player.money:
            print('You don\'t have anough money for this bet')
            continue
        player.bet(bet_amount)
        # Populate dealer's and player's lists/hands
        dealer_cards = [dealer.give_cards() for i in range(2)]
        player_cards = [dealer.give_cards() for i in range(2)]
        # Sum player's and dealer's cards values
        player_value = sum_values(player_cards)
        dealer_value = sum_values(dealer_cards)
        show_cards(player_cards,'Player', dealer_cards)
        # Verify if player's cards sum is a blackjack
        if player_value < 21:   
            while True:
                hit_or_stand = input('Hit |1| or Stand |2|? ')
                try:
                    hit_or_stand = int(hit_or_stand)
                except ValueError:
                    print('Wrong value, please enter |1| or |2|')
                    continue
                # If player choose to stand, sum values and break loop
                if hit_or_stand == 2:    
                    print('Total', player_value)
                    break
                player_value = hitting(player_cards)
                # If the sum is 21 or above, break
                if player_value >= 21:
                    break
        else:
            print('Blackjack!')
        show_cards(dealer_cards, 'Dealer')
        # Verify if dealer's cards sum is a blackjack
        if dealer_value < 21:
            while True:
                if dealer_value >= 17 or player_value > 21:
                    print('Total', dealer_value)
                    break
                dealer_value = hitting(dealer_cards)
                if dealer_value >= 17:
                    break
        else:
            print('Blackjack!')
        # Check all the winning and losing posibilities after getting cards values
        if player_value > 21:
            print('Player bust!')
            dealer.t_g_money(bet_amount, 'take')
        else:
            if dealer_value > 21:
                print('Dealer bust! Player win!')
                player.receive_money(dealer.t_g_money(bet_amount, 'give'))
            elif player_value > dealer_value:
                print('Player win!')
                player.receive_money(dealer.t_g_money(bet_amount, 'give'))
            elif player_value == dealer_value:
                print('Draw!')
                player.receive_money(bet_amount)
            else:
                print('Dealer win!')
                dealer.t_g_money(bet_amount, 'take')
        # Break while loop if player don't have more money
        if player.money == 0:
            print('You don\'t have enough money to keep playing.')
            break
    # Select only the first character of what was inserted in upper case
    play = input('Do you want to play again? Y or N ')[0].upper()
    if play == 'N':        
        break
