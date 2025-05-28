import flet as ft


def main(page: ft.Page):
    page.title = "Mini Project 1"

    counter = ft.Text(value="0", style="display-large")

    def increase(e):
        counter.value = str(int(counter.value) + 1)
        counter.update()

    def decrease(e):
        counter.value = str(int(counter.value) - 1)
        counter.update()

    btn_add = ft.ElevatedButton("+", on_click=increase)
    btn_subtract = ft.ElevatedButton("-", on_click=decrease)
    page.add(
        counter,
        ft.Row([
            btn_subtract,
            btn_add,
            ft.ElevatedButton("Reset", on_click=lambda e: setattr(counter, "value", "0") or counter.update())
        ]

        )
    )

ft.app(target=main)
