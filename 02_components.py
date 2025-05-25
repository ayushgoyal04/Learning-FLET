import flet as ft

def main(page: ft.Page):
    page.title = "My app"

    page.add(
        ft.Text("Hello World"),
        ft.TextField(label="Username", hint_text = "Enter your username"),
        ft.Button("Login"), # 4 types of button-> outline, text, elevated
        ft.Checkbox(label="buy me a coffee"),
        ft.Switch(label="dark mode"),
        ft.Dropdown(label="Branch", options=[
            ft.dropdown.Option("CSE"),
            ft.dropdown.Option("AI-ML"),
            ft.dropdown.Option("DS"),
            ft.dropdown.Option("Cyber"),
        ]),
        ft.Slider(min=0, max=10, divisions=10),
        ft.Container(
            content=ft.Icon(ft.Icons.HOME),
            bgcolor="black",
            margin=20,
            padding=5,
            border_radius=10,
        ),
    )


ft.app(target=main)
