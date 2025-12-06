# Advanced Tic-Tac-Toe AI Game (Python)

## 📋 Overview

An advanced, feature-rich Tic-Tac-Toe game implemented in Python with an intelligent AI opponent. This project demonstrates professional Python development practices including algorithm optimization, persistent data storage, type hints, and advanced game theory concepts. Players can compete against AI at three difficulty levels using the Minimax algorithm with Alpha-Beta Pruning.

## 🎯 Project Objectives

This project showcases:
- Implementation of sophisticated game logic and state management
- Advanced AI decision-making using Minimax with Alpha-Beta Pruning
- Persistent data storage and game statistics tracking
- Professional code architecture using modern Python features
- Type hints and dataclasses for clean, maintainable code
- Terminal UI enhancement with color coding
- Transposition table optimization for algorithm performance

## 📦 Requirements

Python 3.7 or higher

### Dependencies
```
colorama>=0.4.3
tabulate>=0.9.0
```

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project
```bash
git clone <repository-url>
cd tictactoe-ai
```

### Step 2: Install Dependencies
```bash
pip install colorama tabulate
```

Or install from requirements file:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Game
```bash
python tictactoe.py
```

## 🎮 How to Play

### Main Menu
When you launch the game, you'll see a menu with the following options:
1. **Play Game (Hard)** - Play against unbeatable AI using full Minimax
2. **Play Game (Medium)** - Play against semi-intelligent AI (balanced difficulty)
3. **Play Game (Easy)** - Play against random AI (easiest)
4. **View Statistics** - Display your game statistics and history
5. **Exit** - Close the game

### Game Rules
- The board consists of a 3x3 grid with positions numbered 0-8
- You play as **X** (green), AI plays as **O** (red)
- Players alternate turns, placing their symbol on empty squares
- First player to get three in a row (horizontally, vertically, or diagonally) wins
- If all positions are filled without a winner, the game ends in a draw
- You can choose whether to play first or second

### Example Gameplay
```
Position numbers:
     |     |     
  0  |  1  |  2  
_____|_____|_____
     |     |     
  3  |  4  |  5  
_____|_____|_____
     |     |     
  6  |  7  |  8  

Your turn (X):
Enter your move (0-8): 4
```

## 🧠 AI Algorithm: Minimax with Alpha-Beta Pruning

### How Minimax Works

The Minimax algorithm is a recursive game-solving technique that evaluates all possible future game states:

1. **Recursive Exploration**: For each available move, simulate the move and evaluate the resulting board
2. **Score Assignment**: Assign values to terminal states:
   - AI win: +10 points
   - Human win: -10 points
   - Draw: 0 points
3. **Depth Consideration**: Adjust scores based on move depth to prefer quicker wins and delayed losses
4. **Optimal Selection**: 
   - Maximizing (AI's turn): Choose move with highest score
   - Minimizing (Human's turn): Choose move with lowest score

### Alpha-Beta Pruning Optimization

Alpha-Beta Pruning eliminates unnecessary branches from the game tree:

- **Alpha**: Best score the maximizer can guarantee
- **Beta**: Best score the minimizer can guarantee
- **Pruning**: Skip evaluating branches that can't improve the decision

This optimization reduces the number of nodes evaluated from ~362,000 to ~1,000, making the AI respond much faster.

### Transposition Table

The transposition table caches previously evaluated board positions:

- **Key**: Board state represented as a string
- **Value**: Cached minimax score
- **Benefit**: Avoids recalculating the same board position multiple times
- **Performance**: Significantly speeds up AI move calculation

## 🎯 Difficulty Levels

### Easy Mode
- AI makes completely random moves
- Perfect for beginners
- Very beatable

### Medium Mode
- 30% chance of random moves, 70% intelligent moves
- AI only looks ahead 1-2 moves
- Balanced and fun challenge

### Hard Mode (Default)
- Full Minimax algorithm with Alpha-Beta Pruning
- AI is essentially unbeatable
- Can force at best a draw with optimal play
- Uses transposition table for optimization

## 📊 Game Statistics

### What Gets Tracked
- **Total Games Played**: Complete count of all games
- **Your Wins**: Number of games you've won
- **AI Wins**: Number of games AI has won
- **Draws**: Number of drawn games
- **Win Rate**: Percentage of games you've won
- **Average Moves**: Average number of moves per game
- **Game History**: Timestamps and details of each game

### Statistics File
Statistics are automatically saved to `game_stats.pkl` using Python's pickle module:
- Persists across program restarts
- Tracks gameplay over time
- Viewable from the main menu

## 🏗️ Project Architecture

### File Structure
```
tictactoe-ai/
├── tictactoe.py           # Main game implementation
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── game_stats.pkl        # Game statistics (auto-generated)
```

### Class Structure

#### `TicTacToe` Class
Main game class handling all game logic:
- **Board Management**: Represents and manipulates the 3x3 board
- **Win Detection**: Checks all winning combinations
- **AI Logic**: Implements Minimax algorithm
- **Statistics**: Tracks and saves game results
- **UI Display**: Renders colored board and menus

#### `Difficulty` Enum
Defines difficulty levels:
- `EASY`: Random AI
- `MEDIUM`: Semi-intelligent AI
- `HARD`: Minimax AI (default)

#### `GameStats` Dataclass
Stores game statistics:
- Win counts
- Draw counts
- Game history
- Average move calculation

## 🔑 Key Methods

### Core Game Logic
- `is_winner(player)`: Checks if a player has won
- `is_board_full()`: Determines if board is full
- `get_empty_moves()`: Returns available positions
- `evaluate()`: Scores current board state

### AI Decision Making
- `minimax(depth, is_maximizing, alpha, beta)`: Core algorithm with pruning
- `get_best_move()`: Selects optimal move based on difficulty
- `get_board_state()`: Creates string representation for caching

### Game Flow
- `make_human_move()`: Handles player input with validation
- `make_ai_move()`: Executes AI move with thinking animation
- `play()`: Main game loop
- `reset()`: Resets board for new game

### Statistics
- `save_stats()`: Persists statistics to file
- `load_stats()`: Loads statistics from file
- `record_game(result)`: Records game outcome
- `display_stats()`: Shows statistics in table format

## 🛠️ Technologies & Libraries Used

### Core Python
- **typing**: Type hints for better code quality
- **dataclasses**: Clean data structure definitions
- **enum**: Type-safe difficulty levels
- **pathlib**: Modern file path handling
- **datetime**: Game timestamp tracking

### Third-Party Libraries
- **colorama**: Terminal color output (cross-platform)
  - Green for human moves
  - Red for AI moves
  - Cyan for prompts
- **tabulate**: Professional table formatting for statistics
  - Displays stats with fancy_grid style
  - Clean, readable output

### Built-in Modules
- **os**: Screen clearing (cross-platform)
- **sys**: System exit handling
- **time**: Delay for AI thinking animation
- **json**: Data serialization support
- **pickle**: Binary statistics serialization
- **random**: Random selection for Easy/Medium modes
- **collections**: defaultdict support

## 📈 Game Statistics Display

Statistics are displayed in a professional table format:

```
==================================================
          GAME STATISTICS
==================================================

Metric           Value
───────────────────────────────
Total Games      15
Your Wins        2
AI Wins          12
Draws            1
Win Rate         13.3%
Average Moves    6.2
```

## 🎮 User Interface Features

### Color-Coded Output
- **Green**: Your moves and prompts
- **Red**: AI moves and losses
- **Yellow**: AI thinking and draws
- **Cyan**: Main prompts and dividers

### Board Display
```
  X  |     |  O  
_____|_____|_____
     |  X  |     
_____|_____|_____
  O  |     |     
```

### Menu System
Clean, organized main menu with clear navigation and options.

## 🚀 Performance Optimizations

### Alpha-Beta Pruning
Reduces search space from ~362,000 nodes to ~1,000 nodes:
- Eliminates unnecessary branches
- Significantly faster AI response time
- Same optimal move selection as pure Minimax

### Transposition Table
Caches board evaluation results:
- Prevents recalculation of identical positions
- Uses board state strings as keys
- Dramatically improves performance during game

### Difficulty-Based Lookahead
Different difficulties use different search depths:
- Easy: No lookahead
- Medium: Limited lookahead (1-2 moves)
- Hard: Full lookahead with optimizations

## 💾 Persistent Storage

### Statistics File Format
Uses Python's pickle for binary serialization:
- `game_stats.pkl`: Binary file containing GameStats dataclass
- Survives program restarts
- Tracks complete game history
- Automatically created on first use

### Data Recovery
If statistics file is corrupted:
1. Delete `game_stats.pkl`
2. Run the program again
3. New statistics file will be created

## 🧪 Testing the AI

### Verify AI Strength

1. **Test Blocking**: Make two X's in a row; AI should block immediately
2. **Test Winning**: Create two possible winning moves; AI should choose one
3. **Test Forcing Draws**: Play optimally and try to force a draw against Hard mode
4. **Test Difficulty Variance**: Notice differences in AI behavior across difficulty levels

### Performance Testing

Time AI move calculation at different board states:
- Early game: ~500-1000ms
- Mid game: ~100-300ms
- Late game: ~10-50ms

## 🔧 Configuration

### Modify Difficulty Weights (Medium Mode)
Edit the `get_best_move()` method to adjust Medium difficulty:
```python
if random.random() < 0.3:  # Change 0.3 to adjust randomness
    return random.choice(empty_moves)
```

### Customize Colors
Modify color assignments in `print_board()`:
```python
if cell == 'X':
    return f"{Fore.GREEN}{cell}{Style.RESET_ALL}"
```

Change `Fore.GREEN`, `Fore.RED`, etc. to preferred colors from colorama.

## 📝 Code Quality Features

- **Type Hints**: All functions include type annotations
- **Dataclasses**: Clean data structure with automatic `__init__`
- **Docstrings**: Every method has clear documentation
- **Error Handling**: Try-catch blocks for file operations
- **Input Validation**: Comprehensive validation for player moves
- **Constants**: Winning combinations defined once

## 🎓 Learning Outcomes

After studying this project, you'll understand:
- How Minimax algorithm works in game AI
- Alpha-Beta Pruning optimization techniques
- Transposition tables and memoization
- Modern Python practices (type hints, dataclasses, enums)
- File I/O with pickle serialization
- Terminal UI enhancement with colorama
- Professional project structure

## 🚀 Possible Enhancements

- Add network multiplayer support
- Implement 4x4 or 5x5 board variants
- Create graphical UI with tkinter or pygame
- Add sound effects using pygame.mixer
- Implement opening book for faster AI response
- Add AI vs AI simulation mode
- Create web version with Flask/Django
- Implement machine learning-based AI
- Add undo/redo functionality
- Create tournament mode with bracket system

## 🐛 Troubleshooting

### Colors Not Displaying
- Windows: Install colorama (should auto-init)
- Linux/Mac: Ensure terminal supports ANSI colors

### Statistics Not Saving
- Check file write permissions in current directory
- Ensure `game_stats.pkl` is not corrupted
- Delete and let program recreate it

### AI Taking Too Long
- This is normal for Hard mode on an empty or nearly-empty board
- Medium or Easy mode will respond faster
- Transposition table improves with gameplay

## 📄 License

This project is provided for educational purposes.

## 👨‍💻 Author Notes

This implementation prioritizes clean, readable code and professional Python practices over pure optimization. The code demonstrates how to build a complete game application with persistent storage, multiple difficulty levels, and a polished user experience.

## 🎯 Conclusion

This Advanced Tic-Tac-Toe AI project showcases professional Python development combining game theory, algorithm optimization, data persistence, and user interface design. It's an excellent demonstration of how to build intelligent, feature-rich applications in Python.