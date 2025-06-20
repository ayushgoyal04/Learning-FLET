# Mini Project 13: Login Page

This Flet application creates a basic static login page with a hardcoded username and password.

## Features

- **Input Fields:** Standard text fields for entering a username and password.
- **Password Masking:** The password field masks the input and includes a toggle to reveal the password.
- **Authentication Logic:** A simple check is performed against a hardcoded valid username and password.
- **Feedback Message:** A message is displayed to the user indicating whether the login was successful or not.

## How it Works

1.  **Hardcoded Credentials:**

    - A valid username (`VALID_USERNAME`) is set to `"admin"`.
    - A valid password (`VALID_PASSWORD`) is set to `"123"`.

2.  **Login Function (`login`):**
    - The "Login" button's `on_click` event is connected to the `login` function.
    - This function compares the `value` from the `username` and `password` text fields to the hardcoded valid credentials.
    - **If they match:** The `message` text is set to "Login successful!" in green.
    - **If they don't match:** The `message` text is set to "Invalid username or password." in red.
    - `message.update()` is called to display the feedback to the user.
