# Mini Project 10: Drawing Canvas

This Flet application creates a simple pixel drawing canvas using a grid of containers.

## Features

- **Pixel Grid:** A 30x30 grid of clickable cells serves as the drawing canvas.
- **Drawing:** Click on any cell to "paint" it black.
- **Clear Canvas:** A "Clear Canvas" button resets the entire grid, turning all cells back to white.

## How it Works

1.  **Grid Creation:**

    - The canvas is created by programmatically generating a 2D list (`grid`) of `ft.Container` objects.
    - Each `Container` is styled to be a small square (`15x15` pixels) with a white background and a black border, acting as a "cell".
    - The grid is then rendered on the page by creating a `ft.Column` of `ft.Row`s, effectively building the visual grid structure.

2.  **Painting (`paint_cell` function):**

    - Each cell's `on_click` event is bound to the `paint_cell` function.
    - When a cell is clicked, `paint_cell` is called, and the `e.control` argument refers to the specific `Container` that was clicked.
    - `e.control.bgcolor` is set to `ft.Colors.BLACK`, changing the cell's color.
    - `e.control.update()` is called to refresh just that one cell, making the drawing process efficient.

3.  **Clearing the Canvas (`clear_canvas` function):**
    - The "Clear Canvas" button is linked to the `clear_canvas` function.
    - This function iterates through every cell in the `grid`, resets its `bgcolor` to `ft.Colors.WHITE`, and calls `cell.update()` for each.
    - Finally, `page.update()` is called to ensure all changes are rendered.
