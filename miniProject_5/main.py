import flet as ft
import random

def generate_number():
    return random.randint(1, 100)


def main(page: ft.Page):
    # initialize the game
    page.title = "Guess the Number Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # call the function to generate a random number
    number_to_guess = generate_number()
    no_of_guesses = 0

    # take the user's guess, and add the button to check the guess
    input_field = ft.TextField(label="Enter your guess (1-100): ", keyboard_type=ft.KeyboardType.NUMBER, autofocus=True)
    guess_btn = ft.ElevatedButton("Guess", on_click=lambda e: check_guess(input_field, result_text))
    result_text = ft.Text()
    reset_btn = ft.ElevatedButton("Start New Game", on_click=lambda e: reset_game())

    def reset_game():
        input_field.value = ""
        result_text.value = ""
        input_field.disabled = False
        input_field.focus()
        input_field.update()
        result_text.update()
        global number_to_guess, no_of_guesses
        number_to_guess = generate_number()
        no_of_guesses = 0
        page.update()

    # function to check the user's guess
    def check_guess(input_field, result_text):
        nonlocal no_of_guesses
        if input_field.value.isdigit():
            guess = int(input_field.value)
            if guess < 1 or guess > 100:
                result_text.value = "Please enter a number between 1 and 100."
                input_field.value = ""
                input_field.focus()
            elif guess < number_to_guess:
                no_of_guesses += 1
                result_text.value = f"Too low! The number is higher than: {guess}. Number of attempts: {no_of_guesses}"
            elif guess > number_to_guess:
                no_of_guesses += 1
                result_text.value = f"Too high! The number is lower than {guess}. Number of attempts: {no_of_guesses}"
            else:
                no_of_guesses += 1
                result_text.value = f"Congratulations! You've guessed the number {number_to_guess} in {no_of_guesses} tries."
                input_field.disabled = True
                guess_btn.disabled = True
        else:
            result_text.value = "Please enter a valid number."
            input_field.value = ""
            input_field.focus()

        page.update()

    page.add(input_field, guess_btn, result_text, reset_btn)

ft.app(target=main)
