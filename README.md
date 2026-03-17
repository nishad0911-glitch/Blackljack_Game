# 🃏 Blackjack Python CLI
A classic, object-oriented implementation of Blackjack (21) designed to run directly in your terminal. This project demonstrates clean Python architecture, separation of concerns, and robust game logic.

## 🚀 Quick Start
To get the game running on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nishad0911-glitch/Blackljack_Game.git
   cd blackjack-python
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## 🛠 Project Structure
The code is broken down into modular components to make it easy to maintain and scale:

* **`main.py`**: The entry point. Manages the game loop, win/loss conditions, and player bankroll.
* **`blackjack_logic.py`**: Contains the core classes:
    * `Card`: Defines suit and rank.
    * `Deck`: Handles shuffling and dealing.
    * `Hand`: Manages card totals and Ace adjustments.
    * `Chips`: Tracks the player's betting balance.
* **`game_utils.py`**: Helper functions for terminal input/output and displaying the "table" view.

## 🎮 How to Play
1. **The Goal**: Get your hand value as close to 21 as possible without going over (busting).
2. **Setup**: You start with **100 chips**.
3. **The Deal**: You and the Dealer are dealt two cards. One of the Dealer's cards remains hidden.
4. **Your Turn**: 
   * **Hit (H)**: Take another card.
   * **Stand (S)**: Keep your current total and end your turn.
5. **The Dealer**: The Dealer must hit until their cards total **17 or higher**.
6. **Aces**: Automatically adjust from **11 to 1** if your hand exceeds 21.



