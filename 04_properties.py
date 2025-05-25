import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            # content=ft.Text("Adding properties i.e. css", size=16),
            # we can add multiple content in container by making a list->
            content=ft.ListView(controls=[
                ft.Text("Hello 1", color="black", weight="bold", size=24, font_family="Arial"),
                ft.Text("Hello 2"),
            ]),
            bgcolor="blue", # you can also give hex values
            margin=20,
            padding=5,
            border_radius=10,
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
