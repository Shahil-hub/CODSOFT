import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
from collections import defaultdict
import pickle
import random
from colorama import Fore, Back, Style, init
from tabulate import tabulate

init(autoreset=True)

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

@dataclass
class GameStats:
    human_wins: int = 0
    ai_wins: int = 0
    draws: int = 0
    total_games: int = 0
    average_moves: float = 0.0
    games_played: List[dict] = None
    
    def __post_init__(self):
        if self.games_played is None:
            self.games_played = []
    
    def to_dict(self):
        return {
            'human_wins': self.human_wins,
            'ai_wins': self.ai_wins,
            'draws': self.draws,
            'total_games': self.total_games,
            'average_moves': self.average_moves
        }

class TicTacToe:
    def __init__(self, difficulty: Difficulty = Difficulty.HARD):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.difficulty = difficulty
        self.move_history = []
        self.stats = GameStats()
        self.stats_file = Path('game_stats.pkl')
        self.transposition_table = {}
        self.load_stats()
    
    def load_stats(self):
        """Load game statistics from file"""
        try:
            if self.stats_file.exists():
                with open(self.stats_file, 'rb') as f:
                    self.stats = pickle.load(f)
        except Exception as e:
            print(f"{Fore.RED}Error loading stats: {e}{Style.RESET_ALL}")
    
    def save_stats(self):
        """Save game statistics to file"""
        try:
            with open(self.stats_file, 'wb') as f:
                pickle.dump(self.stats, f)
        except Exception as e:
            print(f"{Fore.RED}Error saving stats: {e}{Style.RESET_ALL}")
    
    def display_stats(self):
        """Display game statistics in table format"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}          GAME STATISTICS")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")
        
        stats_data = [
            ["Total Games", self.stats.total_games],
            ["Your Wins", f"{Fore.GREEN}{self.stats.human_wins}{Style.RESET_ALL}"],
            ["AI Wins", f"{Fore.RED}{self.stats.ai_wins}{Style.RESET_ALL}"],
            ["Draws", f"{Fore.YELLOW}{self.stats.draws}{Style.RESET_ALL}"],
            ["Win Rate", f"{(self.stats.human_wins/max(1, self.stats.total_games)*100):.1f}%"],
            ["Average Moves", f"{self.stats.average_moves:.1f}"]
        ]
        
        print(tabulate(stats_data, headers=["Metric", "Value"], tablefmt="fancy_grid"))
        print()
    
    def print_board(self):
        """Print the game board with colors"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        
        def color_cell(cell):
            if cell == 'X':
                return f"{Fore.GREEN}{cell}{Style.RESET_ALL}"
            elif cell == 'O':
                return f"{Fore.RED}{cell}{Style.RESET_ALL}"
            else:
                return cell
        
        board_display = [
            f"  {color_cell(self.board[0])}  |  {color_cell(self.board[1])}  |  {color_cell(self.board[2])}",
            "_____|_____|_____",
            f"  {color_cell(self.board[3])}  |  {color_cell(self.board[4])}  |  {color_cell(self.board[5])}",
            "_____|_____|_____",
            f"  {color_cell(self.board[6])}  |  {color_cell(self.board[7])}  |  {color_cell(self.board[8])}"
        ]
        
        for line in board_display:
            print(line)
        print()
    
    def print_positions(self):
        """Print position guide"""
        print(f"{Fore.CYAN}Position numbers:{Style.RESET_ALL}")
        print("     |     |     ")
        print("  0  |  1  |  2  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  3  |  4  |  5  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  6  |  7  |  8  ")
        print("     |     |     \n")
    
    def is_winner(self, player: str) -> bool:
        """Check if player is winner"""
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combos)
    
    def is_board_full(self) -> bool:
        """Check if board is full"""
        return ' ' not in self.board
    
    def get_empty_moves(self) -> List[int]:
        """Get list of empty positions"""
        return [i for i in range(9) if self.board[i] == ' ']
    
    def get_board_state(self) -> str:
        """Get board state as string for transposition table"""
        return ''.join(self.board)
    
    def evaluate(self) -> int:
        """Evaluate board position"""
        if self.is_winner(self.ai):
            return 10
        elif self.is_winner(self.human):
            return -10
        return 0
    
    def minimax(self, depth: int, is_maximizing: bool, alpha: int = float('-inf'), beta: int = float('inf')) -> int:
        """Minimax with alpha-beta pruning and transposition table"""
        board_state = self.get_board_state()
        
        if board_state in self.transposition_table:
            return self.transposition_table[board_state]
        
        score = self.evaluate()
        
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for move in self.get_empty_moves():
                self.board[move] = self.ai
                score = self.minimax(depth + 1, False, alpha, beta)
                self.board[move] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            for move in self.get_empty_moves():
                self.board[move] = self.human
                score = self.minimax(depth + 1, True, alpha, beta)
                self.board[move] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        
        self.transposition_table[board_state] = best_score
        return best_score
    
    def get_best_move(self) -> Optional[int]:
        """Get best move for AI based on difficulty"""
        empty_moves = self.get_empty_moves()
        
        if self.difficulty == Difficulty.EASY:
            return random.choice(empty_moves) if empty_moves else None
        
        elif self.difficulty == Difficulty.MEDIUM:
            if random.random() < 0.3:
                return random.choice(empty_moves)
            best_score = float('-inf')
            best_move = None
            for move in empty_moves[:5]:
                self.board[move] = self.ai
                score = self.minimax(0, False)
                self.board[move] = ' '
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
        
        else:
            best_score = float('-inf')
            best_move = None
            for move in empty_moves:
                self.board[move] = self.ai
                score = self.minimax(0, False)
                self.board[move] = ' '
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move
    
    def make_human_move(self):
        """Handle human player move"""
        while True:
            try:
                position = int(input(f"{Fore.CYAN}Enter your move (0-8): {Style.RESET_ALL}"))
                if position < 0 or position > 8:
                    print(f"{Fore.RED}Invalid! Please enter a number between 0 and 8.{Style.RESET_ALL}")
                    continue
                if self.board[position] != ' ':
                    print(f"{Fore.RED}That position is already taken!{Style.RESET_ALL}")
                    continue
                self.board[position] = self.human
                self.move_history.append(position)
                break
            except ValueError:
                print(f"{Fore.RED}Invalid input! Please enter a number.{Style.RESET_ALL}")
    
    def make_ai_move(self):
        """Handle AI move"""
        print(f"{Fore.YELLOW}AI is thinking...{Style.RESET_ALL}")
        time.sleep(0.5)
        move = self.get_best_move()
        if move is not None:
            self.board[move] = self.ai
            self.move_history.append(move)
            print(f"{Fore.YELLOW}AI placed O at position {move}{Style.RESET_ALL}\n")
    
    def record_game(self, result: str):
        """Record game results"""
        self.stats.total_games += 1
        
        if result == 'human':
            self.stats.human_wins += 1
        elif result == 'ai':
            self.stats.ai_wins += 1
        else:
            self.stats.draws += 1
        
        game_record = {
            'result': result,
            'timestamp': datetime.now().isoformat(),
            'moves': len(self.move_history),
            'difficulty': self.difficulty.name
        }
        self.stats.games_played.append(game_record)
        
        total_moves = sum(g['moves'] for g in self.stats.games_played)
        self.stats.average_moves = total_moves / self.stats.total_games
        
        self.save_stats()
    
    def play(self):
        """Main game loop"""
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}  Welcome to Advanced Tic-Tac-Toe AI Game")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        self.print_positions()
        
        human_first = input(f"{Fore.CYAN}Do you want to go first? (yes/no): {Style.RESET_ALL}").lower() == 'yes'
        
        current_turn = 'human' if human_first else 'ai'
        
        while True:
            self.print_board()
            
            if current_turn == 'human':
                print(f"{Fore.GREEN}Your turn (X):{Style.RESET_ALL}")
                self.make_human_move()
                
                if self.is_winner(self.human):
                    self.print_board()
                    print(f"{Fore.GREEN}Congratulations! You won!{Style.RESET_ALL}")
                    self.record_game('human')
                    break
            else:
                self.make_ai_move()
                
                if self.is_winner(self.ai):
                    self.print_board()
                    print(f"{Fore.RED}AI won! Better luck next time.{Style.RESET_ALL}")
                    self.record_game('ai')
                    break
            
            if self.is_board_full():
                self.print_board()
                print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
                self.record_game('draw')
                break
            
            current_turn = 'ai' if current_turn == 'human' else 'human'
        
        print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    def reset(self):
        """Reset for new game"""
        self.board = [' ' for _ in range(9)]
        self.move_history = []
        self.transposition_table = {}

def main():
    """Main entry point"""
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"{Fore.CYAN}        TIC-TAC-TOE AI MENU")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")
        print("1. Play Game (Hard)")
        print("2. Play Game (Medium)")
        print("3. Play Game (Easy)")
        print("4. View Statistics")
        print("5. Exit")
        
        choice = input(f"\n{Fore.CYAN}Select an option: {Style.RESET_ALL}").strip()
        
        if choice == '1':
            game = TicTacToe(Difficulty.HARD)
            game.play()
            play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
            if play_again != 'yes':
                continue
            game.reset()
            while play_again == 'yes':
                game.play()
                play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
                if play_again == 'yes':
                    game.reset()
        
        elif choice == '2':
            game = TicTacToe(Difficulty.MEDIUM)
            game.play()
            play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
            if play_again != 'yes':
                continue
            game.reset()
            while play_again == 'yes':
                game.play()
                play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
                if play_again == 'yes':
                    game.reset()
        
        elif choice == '3':
            game = TicTacToe(Difficulty.EASY)
            game.play()
            play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
            if play_again != 'yes':
                continue
            game.reset()
            while play_again == 'yes':
                game.play()
                play_again = input(f"\n{Fore.CYAN}Play again? (yes/no): {Style.RESET_ALL}").lower()
                if play_again == 'yes':
                    game.reset()
        
        elif choice == '4':
            game = TicTacToe()
            game.display_stats()
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        
        elif choice == '5':
            print(f"\n{Fore.CYAN}Thanks for playing!{Style.RESET_ALL}\n")
            sys.exit(0)
        
        else:
            print(f"{Fore.RED}Invalid option! Please try again.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()