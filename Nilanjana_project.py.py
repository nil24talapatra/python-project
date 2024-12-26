import tkinter as tk
import random

# Function to play the game
def play_game(player_choice):
    global player_wins, computer_wins, draws, round_num

    # Mapping player choice to computer choice
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
        draws += 1
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Won!"
        player_wins += 1
    else:
        result = "You Lost!"
        computer_wins += 1

    round_num += 1

    # Update the results in the GUI
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Round {round_num}/5\nYour Wins: {player_wins}\nComputer Wins: {computer_wins}\nDraws: {draws}")

    # After 5 rounds, display the final results
    if round_num == 5:
        final_result = f"Game Over!\nYour Wins: {player_wins}\nComputer Wins: {computer_wins}\nDraws: {draws}"
        result_label.config(text=final_result)
        play_button.config(state=tk.DISABLED)

# Initialize game variables
player_wins = 0
computer_wins = 0
draws = 0
round_num = 1

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create the labels for showing results and score
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Round 1/5\nYour Wins: 0\nComputer Wins: 0\nDraws: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", width=10, height=2, font=("Arial", 12), command=lambda: play_game("Rock"))
rock_button.pack(side=tk.LEFT, padx=20, pady=20)

paper_button = tk.Button(root, text="Paper", width=10, height=2, font=("Arial", 12), command=lambda: play_game("Paper"))
paper_button.pack(side=tk.LEFT, padx=20, pady=20)

scissors_button = tk.Button(root, text="Scissors", width=10, height=2, font=("Arial", 12), command=lambda: play_game("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

# Start the GUI event loop
root.mainloop()
