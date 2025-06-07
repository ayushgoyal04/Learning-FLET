import flet as ft
import datetime, time

def main(page : ft.Page):
    page.title = "Digital clock app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    time_display = ft.Text(
        value = "00:00:00",
        size=50,
        key="clock",
        color=ft.Colors.CYAN_200,
        weight=ft.FontWeight.BOLD
        )

    page.add(
        time_display
    )

    def update_clock():
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            time_display.value = now
            page.update()
            time.sleep(1)

    page.run_thread(update_clock)
ft.app(target=main)
