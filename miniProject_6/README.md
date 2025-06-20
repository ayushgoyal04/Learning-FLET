# Mini Project 6: Character Counter

This Flet application provides a real-time character counter for text entered into a text field.

## Features

- **Text Input:** A multiline `TextField` allows users to enter or paste any amount of text.
- **Live Character Count:** The application instantly calculates and displays the total number of characters in the text field as the user types.
- **Simple Interface:** The UI is clean and straightforward, consisting only of the text input area and the character count display.

## How it Works

The application's core logic is handled by the `update_char_count` function, which is bound to the `on_change` event of the `TextField`.

1.  A `TextField` (`text_input`) is created for user input.
2.  A `Text` control (`char_count`) is created to display the count.
3.  The `text_input.on_change` property is set to the `update_char_count` function. This means `update_char_count` is called automatically every time the content of the text field changes.
4.  Inside `update_char_count(e)`:
    - `len(text_input.value)` calculates the length of the current string in the text field.
    - The `value` of the `char_count` text control is updated with the new count.
    - `char_count.update()` refreshes the display to show the latest count.
