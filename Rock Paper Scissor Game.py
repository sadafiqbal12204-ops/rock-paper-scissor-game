import random

# Constants for text styling
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Maps shorthand and plural inputs to standard choices
ALIASES = {
    "r": "rock",
    "rock": "rock",
    "p": "paper",
    "paper": "paper",
    "s": "scissor",
    "scissor": "scissor",
    "scissors": "scissor",
}

# Maps winning move -> (losing move, action text)
WIN_RULES = {
    "rock": ("scissor", "Rock crushes Scissor"),
    "paper": ("rock", "Paper covers Rock"),
    "scissor": ("paper", "Scissor cuts Paper"),
}


def print_banner(title: str) -> None:
  print("\n" + "=" * 60)
  print(title.center(60))
  print("=" * 60 + "\n")


def play_game() -> None:
  print_banner("WELCOME TO ROCK PAPER SCISSOR GAME!")

  choices = ["rock", "paper", "scissor"]
  computer_score = 0
  ties = 0
  attempts = 0

  while True:
    raw_input = (
        input(f"{BOLD}Choose (Rock/r, Paper/p, Scissor/s) or 'q' to quit: {RESET}")
        .strip()
        .lower()
    )

    if raw_input in ("q", "quit"):
      print("\nThanks for playing! Exiting game.")
      return

    if raw_input not in ALIASES:
      print(
          f"{YELLOW}Invalid input. Please enter Rock, Paper, or Scissor.{RESET}\n"
      )
      continue

    user_choice = ALIASES[raw_input]
    comp_choice = random.choice(choices)
    attempts += 1

    print("\n" + "-" * 60)
    print(f"Round #{attempts}")
    print(f"User choice     : {user_choice.capitalize()}")
    print(f"Computer choice : {comp_choice.capitalize()}")
    print("-" * 60)

    if user_choice == comp_choice:
      ties += 1
      print(
          f"{BOLD}{YELLOW}{'Both chose the same :: Match Tie'.center(60)}{RESET}\n"
      )
    elif WIN_RULES[user_choice][0] == comp_choice:
      action = WIN_RULES[user_choice][1]
      print(f"{BOLD}{GREEN}{f'{action}, User Wins!'.center(60)}{RESET}\n")
      break
    else:
      computer_score += 1
      action = WIN_RULES[comp_choice][1]
      print(f"{BOLD}{RED}{f'{action}, Computer Wins!'.center(60)}{RESET}\n")

  print_banner(f"Game Over! User won in {attempts} round(s)!")
  print(
      f"Final Stats -> User Wins: 1 | Computer Wins: {computer_score} | Ties: {ties}\n"
  )


if __name__ == "__main__":
  play_game()
