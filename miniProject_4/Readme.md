# Mini Project 4: Dice Roller and Coin Toss

This Flet application provides a simple interface to simulate rolling a six-sided die and tossing a coin.

## Features

- **Roll Dice:** Click the "Roll Dice" button to get a random number from 1 to 6, along with a corresponding Unicode die face (e.g., ⚀, ⚁).
- **Toss Coin:** Click the "Toss Coin" button to get a "Heads" or "Tails" result.
- **Display Result:** The outcome of the dice roll or coin toss is displayed on the screen.
- **Reset:** A "Reset" button clears the result text.

## How it Works

The application has three main functions triggered by button clicks:

- `roll_dice(e)`:

  - Generates a random integer between 1 and 6 using `random.randint(1, 6)`.
  - Uses a dictionary `dice_faces` to map the number to a Unicode character representing the die face.
  - Updates a `Text` control (`result_text`) with the outcome.

- `toss_coin(e)`:

  - Uses `random.choice(['Heads', 'Tails'])` to simulate a coin toss.
  - Updates the `result_text` with the result.

- `reset_result(e)`:
  - Clears the `result_text` value.

The UI is built with `ElevatedButton` controls for each action and a `Text` control to show the results. `page.update()` is called in each function to reflect the changes in the UI.
