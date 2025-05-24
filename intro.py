import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    text = ft.Text("Hello World", size=50)

    page.add(text)

# main is the function, not the file
# ft.app(target=main, view=ft.WEB_BROWSER)
ft.app(target=main)
