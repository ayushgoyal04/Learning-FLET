import re
import flet as ft

def main(page: ft.Page):
    page.title = "password strength checker"
    page.theme_mode= "light"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    result_text = ft.Text(size=20, weight="bold")

    def check_password_strength(e):
        password = e.control.value
        strength = 0
        if len(password) >= 8:
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength+=1
        if re.search(r"\d", password):
            strength+=1
        if re.search(r"[!@#$%^&*~_+=]", password):
            strength+=1

        if strength <=2:
            result_text.value="Weak"
            result_text.color="red"
        elif strength ==3 or strength==4:
            result_text.value="Medium"
            result_text.Color="orange"
        else:
            result_text.value="Strong"
            result_text.color="green"
        page.update()

    password_input = ft.TextField(
        label="Enter pass",
        password=True,
        can_reveal_password=True,
        on_change=check_password_strength,
        width=300)
    page.add(password_input, result_text)

ft.app(target=main)
