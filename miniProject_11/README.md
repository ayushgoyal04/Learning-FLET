# Mini Project 11: Password Strength Checker

This Flet application provides a real-time password strength checker that evaluates a password as the user types.

## Features

- **Live Feedback:** The strength of the password is checked and displayed instantly on every character change.
- **Strength Levels:** The application categorizes the password into three levels: "Weak" (red), "Medium" (orange), and "Strong" (green).
- **Password Masking:** The input is a `TextField` with `password=True`, which masks the characters. It also includes an icon to reveal the password.

## How it Works

The core logic resides in the `check_password_strength` function, which is triggered by the `on_change` event of the password `TextField`.

### Strength Criteria

A `strength` score is calculated based on the following rules, with one point awarded for each criterion met:

1.  Is the password length 8 or more characters?
2.  Does it contain at least one uppercase letter (`[A-Z]`)?
3.  Does it contain at least one lowercase letter (`[a-z]`)?
4.  Does it contain at least one digit (`\d`)?
5.  Does it contain at least one special character from the set `!@#$%^&*~_+=`?

### Evaluation

The final `strength` score determines the result:

- **Score <= 2:** "Weak"
- **Score 3 or 4:** "Medium"
- **Score 5:** "Strong"

The `result_text` control is then updated with the appropriate value and color, and `page.update()` is called to refresh the UI.
