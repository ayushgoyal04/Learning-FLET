import flet as ft
def main(page:ft.Page):
    page.title = "Login page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = ft.TextField(label="Username", autofocus=True, width=300)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300)

    message = ft.Text("")

    VALID_USERNAME = "admin"
    VALID_PASSWORD = "123"

    def login(e):
        if username.value == VALID_USERNAME and password.value == VALID_PASSWORD:
            message.value = "Login successful!"
            message.color = "green"
        else:
            message.value = "Invalid username or password."
            message.color = "red"
        message.update()
    login_button = ft.ElevatedButton("Login", on_click=login)
    page.add(
        username,
        password,
        login_button,
        message
    )

ft.app(target=main)
