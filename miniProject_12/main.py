import flet as ft

def main(page: ft.Page):
    page.title = "multiplication table generator"
    page.padding = 30
    number_input = ft.TextField(
        label="Enter a number",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200
    )
    result = ft.Column()

    def generate_table(e):
        result.controls.clear()
        try:
            number = int(number_input.value)
            for i in range(1, 11):
                result.controls.append(ft.Text(f"{number} x {i} = {number * i}"))
        except ValueError:
            result.controls.append(ft.Text("Please enter a valid number."))
        result.update()

    generate_btn = ft.ElevatedButton("Generate Table", on_click=generate_table)

    page.add(number_input, generate_btn, result)

ft.app(target=main)
