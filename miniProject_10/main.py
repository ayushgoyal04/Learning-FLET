import flet as ft

def main(page: ft.Page):
    page.title = "Drawing canvas"
    rows, cols = 30, 30
    cell_size = 15
    selected_color = ft.Colors.BLACK

    grid = []

    def paint_cell(e):
        e.control.bgcolor = selected_color
        e.control.update()

    for _ in range(rows):
        row = []
        for _ in range(cols):
            cell = ft.Container(
                width=cell_size,
                height=cell_size,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.BLACK),
                on_click=paint_cell
            )
            row.append(cell)
        grid.append(row)

    grid_ui = ft.Column(
        [
        ft.Row(row, spacing=0) for row in grid
        ], spacing=0
    )

    def clear_canvas(e):
        for row in grid:
            for cell in row:
                cell.bgcolor = ft.Colors.WHITE
                cell.update()

        page.update()

    page.add(
        grid_ui,
        ft.ElevatedButton("Clear Canvas", on_click=clear_canvas),
    )


ft.app(target=main)
