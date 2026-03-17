def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f'How many chips would you like to bet? (Balance: {chips.total}): '))
        except ValueError:
            print('Sorry, please enter a number.')
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you only have {chips.total} chips!")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def show_some(player, dealer):
    print("\n--- Dealer's Hand ---")
    print(" <card hidden>")
    print(f" {dealer.cards[1]}")
    print("\n--- Player's Hand ---")
    print(*player.cards, sep='\n')
    print(f"Value: {player.value}")

def show_all(player, dealer):
    print("\n--- Dealer's Hand ---")
    print(*dealer.cards, sep='\n')
    print(f"Dealer Value: {dealer.value}")
    print("\n--- Player's Hand ---")
    print(*player.cards, sep='\n')
    print(f"Player Value: {player.value}")