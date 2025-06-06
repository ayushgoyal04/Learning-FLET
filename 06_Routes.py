import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/",[
                ft.Text("Home"),
                ft.ElevatedButton("Go to About", on_click=lambda _: page.go("/about"))
                ]))
        elif page.route == "/about":
            page.views.append(ft.View("/about", [
                ft.Text("About"),
                ft.ElevatedButton("Go to Home", on_click=lambda _: page.go("/"))
            ]))

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
