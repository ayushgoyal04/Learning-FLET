# Mini Project 2: Theme Switcher

This Flet application demonstrates how to switch between light and dark themes.

## Features

- **Theme Toggle:** A switch control allows the user to toggle between `light` and `dark` mode for the application window.
- **Dynamic Text Update:** The application displays text that indicates the current theme (`"light"` or `"dark"`), and this text updates automatically when the theme is changed.

## How it Works

The application initializes in `light` mode. A `Switch` control is provided with a label "Dark mode". The `on_change` event of this switch is tied to the `theme_change` function.

When the switch is toggled, the `theme_change` function checks the switch's value.

- If it's `True`, the page's `theme_mode` is set to `ft.ThemeMode.DARK`.
- If it's `False`, it's set back to `ft.ThemeMode.LIGHT`.

After changing the theme, a `Text` control is updated to show the current theme's name, and `page.update()` is called to apply the changes to the UI.
