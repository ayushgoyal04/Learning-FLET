# Mini Project 5: Guess the Number Game

This Flet application is a classic "Guess the Number" game where the player tries to guess a randomly generated number between 1 and 100.

## Features

- **Random Number Generation:** A secret number between 1 and 100 is generated at the start of each game.
- **User Input:** A text field allows the player to enter their guess.
- **Feedback:** The application provides feedback after each guess, telling the player if their guess was "Too high!" or "Too low!".
- **Attempt Counter:** The number of guesses is tracked and displayed.
- **Win Condition:** When the player guesses the correct number, a congratulatory message is shown with the total number of attempts.
- **New Game:** A "Start New Game" button allows the player to reset the game at any time and try to guess a new number.
- **Input Validation:** The application checks if the input is a valid number within the 1-100 range.

## How it Works

1.  **Initialization:**

    - A random number is generated using `random.randint(1, 100)` and stored in `number_to_guess`.
    - A counter for guesses, `no_of_guesses`, is initialized to 0.

2.  **Gameplay (`check_guess` function):**

    - The player enters a number in the `TextField` and clicks the "Guess" button.
    - The input is validated to ensure it's a digit.
    - The guessed number is compared to `number_to_guess`:
      - If too low, a "Too low!" message is shown.
      - If too high, a "Too high!" message is shown.
      - If correct, a success message is displayed, and the input field and guess button are disabled.
    - The number of guesses is incremented with each attempt.

3.  **Resetting the Game (`reset_game` function):**
    - Clicking the "Start New Game" button calls `reset_game`.
    - This function resets the input field, result text, and re-enables the input.
    - Crucially, it generates a new random number and resets the guess counter, starting a fresh game.
