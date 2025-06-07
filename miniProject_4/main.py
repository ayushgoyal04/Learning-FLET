import flet as ft
import random

def main(page: ft.Page):
    page.title = "dice and toss app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    result_text = ft.Text("", size=20, color=ft.Colors.GREEN_900)

    # Unicode dice faces 1-6
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }

    def roll_dice(e):
        number = random.randint(1, 6)
        face = dice_faces[number]
        result_text.value = f"You rolled a {number}! {face}"
        page.update()

    def reset_result(e):
        result_text.value = ""
        page.update()

    def toss_coin(e):
        result_text.value = f"You tossed a {random.choice(['Heads', 'Tails'])}!"
        page.update()

    page.add(
        ft.Text("Click the button to roll the dice!", size=30, color=ft.Colors.BLUE_900, weight=ft.FontWeight.BOLD),
        ft.Row([

        ft.ElevatedButton(text="Roll Dice", on_click=roll_dice),
        ft.ElevatedButton(text="Toss Coin", on_click=toss_coin)
        ], alignment=ft.MainAxisAlignment.CENTER

        ),
        ft.ElevatedButton(text="Reset", on_click=reset_result),
        result_text
    )

ft.app(target=main)
