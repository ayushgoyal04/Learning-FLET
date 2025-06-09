import flet as ft


def main(page: ft.Page):
    page.title="character counting"
    text_input = ft.TextField(label="Enter text: ", multiline=True, width=400)
    char_count =  ft.Text("Character count: 0", size=20)

    def update_char_count(e):
        count = len(text_input.value)
        char_count.value = f"Character count: {count}"
        char_count.update()

    text_input.on_change = update_char_count

    page.add(
        text_input,
        char_count,
    )

ft.app(target=main)
