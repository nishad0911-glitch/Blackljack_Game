from blackjack_logic import Deck, Hand, Chips
from game_utils import take_bet, hit, show_some, show_all

def main():
    # Initialize chips outside the loop to keep balance between rounds
    player_chips = Chips()
    
    while True:
        print('\nWelcome to BlackJack!')
        
        # Setup Deck & Hands
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
        take_bet(player_chips)
        show_some(player_hand, dealer_hand)
        
        playing = True
        while playing:
            action = input("\nWould you like to (H)it or (S)tand? ").lower()
            
            if action.startswith('h'):
                hit(deck, player_hand)
                show_some(player_hand, dealer_hand)
                
                if player_hand.value > 21:
                    print("\nPLAYER BUSTS!")
                    player_chips.lose_bet()
                    playing = False
            elif action.startswith('s'):
                print("Player stands. Dealer is playing...")
                playing = False
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        # Dealer Logic (if player didn't bust)
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            show_all(player_hand, dealer_hand)
            
            if dealer_hand.value > 21:
                print("DEALER BUSTS! YOU WIN!")
                player_chips.win_bet()
            elif dealer_hand.value > player_hand.value:
                print("DEALER WINS!")
                player_chips.lose_bet()
            elif dealer_hand.value < player_hand.value:
                print("PLAYER WINS!")
                player_chips.win_bet()
            else:
                print("It's a PUSH (Tie)!")

        print(f"\nNew Balance: {player_chips.total}")
        
        if player_chips.total == 0:
            print("You're broke! Game over.")
            break
            
        if input("Play again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()