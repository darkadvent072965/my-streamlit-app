import streamlit as st
import random

def determine_winner(user_choice, computer_choice, rigging=0):
    if rigging == 1:
        return "user"
    elif rigging == 2:
        return "computer"
    else:
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        else:
            return "computer"

def play_rps_game(name, rigging=0):
    user_wins = 0
    computer_wins = 0
    rounds_played = 0
    results = []

    while user_wins < 6 and computer_wins < 6 and rounds_played < 10:
        st.write(f"Round {rounds_played + 1} — Make your move!")
        user_choice = st.selectbox("Choose your move:", ["rock", "paper", "scissors"], key=f"rps_{rounds_played}")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        winner = determine_winner(user_choice, computer_choice, rigging)
        rounds_played += 1
        if winner == "user":
            user_wins += 1
            results.append(f"You chose {user_choice}, computer chose {computer_choice}. You win this round!")
        elif winner == "computer":
            computer_wins += 1
            results.append(f"You chose {user_choice}, computer chose {computer_choice}. You lose this round.")
        else:
            results.append(f"Both chose {user_choice}. It's a tie!")

        if user_wins >= 6 or computer_wins >= 6 or rounds_played >= 10:
            break

    results.append(f"Final score — You: {user_wins}, Computer: {computer_wins}")
    if user_wins > computer_wins:
        results.append(f"Congratulations {name}! You won the best of 10!")
    else:
        results.append("Sorry, the computer won the best of 10!")

    return "\n".join(results)

# Streamlit UI
st.title("Rock Paper Scissors Game")

player_name = st.text_input("Enter your name:")
rig = st.selectbox("Do you want to rig the game? (for testing)", [0,1,2])

if player_name and st.button("Play Best of 10"):
    result = play_rps_game(player_name, rigging=rig)
    st.text(result)
