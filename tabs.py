import flet as ft

def main(page: ft.Page):
    page.add(
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
        # ft.Text("This will no be part of any tab")
        # ft.ListView(controls=[
        #     ft.Text("List 1"),
        #     ft.Text("List 2"),
        #     ft.Text("List 3"),
        #     ft.Text("List 4"),

        # ])
    )
ft.app(target=main)
