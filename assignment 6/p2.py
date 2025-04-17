import random

class RockPaperScissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return 'user'
        else:
            self.computer_wins += 1
            return 'computer'

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")
        while self.current_round <= self.total_rounds:
            print(f"\nRound {self.current_round} of {self.total_rounds}")
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            while user_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice. Try again.")
                user_choice = input("Enter rock, paper, or scissors: ").lower()
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            winner = self.find_winner(user_choice, computer_choice)
            if winner == 'tie':
                print("It's a tie!")
            elif winner == 'user':
                print("You win this round!")
            else:
                print("Computer wins this round!")
            
            self.current_round += 1
        
        self.check_winner()

    def check_winner(self):
        print("\nGame Over!")
        print(f"Final Score - You: {self.user_wins}, Computer: {self.computer_wins}")
        if self.user_wins > self.computer_wins:
            print("Congratulations! You won the game!")
        elif self.computer_wins > self.user_wins:
            print("Computer wins the game! Better luck next time.")
        else:
            print("It's a tie game!")

# Play the game
rounds = int(input("Enter the number of rounds: "))
game = RockPaperScissors(rounds)
game.play_game()
