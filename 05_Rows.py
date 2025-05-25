import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            content=ft.Row([
                ft.Text("Left"),
                ft.Text("Right"),
            ], alignment="spaceBetween"),
        ),
        ft.Tabs(selected_index=0, tabs=[
            ft.Tab(text="Home",
                   content=ft.Text("This is Home page")
                   ),
            ft.Tab(text="About",
                   content=ft.Text("This is about page")
                   ),
            ft.Tab(text="Contact",
                   content=ft.Text("Contact me")
                   ),
        ]),
    )
ft.app(target=main)
