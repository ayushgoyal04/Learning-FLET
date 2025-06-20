# Mini Project 12: Multiplication Table Generator

This Flet application generates and displays the multiplication table for a number entered by the user.

## Features

- **User Input:** A `TextField` allows the user to enter a number.
- **Table Generation:** A button click triggers the generation of the multiplication table from 1 to 10 for the entered number.
- **Dynamic Display:** The results are displayed cleanly in a column.
- **Input Validation:** The application handles cases where the input is not a valid number.

## How it Works

1.  **Input:** The user enters a number into the `TextField` (`number_input`).
2.  **Button Click:** The "Generate Table" button's `on_click` event is tied to the `generate_table` function.
3.  **`generate_table` Function:**
    - It first clears any previous results from the `result` column (`result.controls.clear()`).
    - It uses a `try-except` block to handle potential `ValueError` if the input is not a valid integer.
    - **If valid:** It converts the input value to an integer. It then loops from 1 to 10, creating a `Text` control for each line of the multiplication table (e.g., "5 x 1 = 5") and appending it to the `result` column.
    - **If invalid:** It adds a single `Text` control to the `result` column with an error message.
4.  **UI Update:** `result.update()` is called to render the newly added text controls on the page.
