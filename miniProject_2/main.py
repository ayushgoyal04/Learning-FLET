import flet as ft

def main(page : ft.Page):
    page.title = "theme switcher app"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def theme_change(e):
        if e.control.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        text.value = "Current theme: " + str(page.theme_mode.value)
        page.update()

    btn = ft.Switch(label= "Dark mode", on_change=theme_change)
    text = ft.Text("Current theme: " + str(page.theme_mode.value), size=40)

    page.add(
        text,
        btn
    )

ft.app(target=main)
