import flet as ft

def main(page:ft.Page):
    page.title = "Text editor"
    page.window_width = 800
    page.window_height = 600
    page.scroll = ft.ScrollMode.AUTO

    text_area = ft.TextField(
        expand=True,
        min_lines= 20,
        hint_text="Type your text here..."
    )

    # calling the file picker function
    file_picker_open = ft.FilePicker()
    file_picker_save_as = ft.FilePicker()

    current_file_path = {"path":None}

    def open_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                with open(file_path, "r",encoding="utf-8") as f:
                    text_area.value = f.read()
                    current_file_path["path"] = file_path
                    page.snack_bar = ft.SnackBar(ft.Text(f"Opened: {file_path}"))
                    page.snack_bar.open= True
                    page.update()
            except Exception as err:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error:{err}", color="red"))
                page.snack_bar.open = True
                page.update()

    def save_as_result(e:ft.FilePickerResultEvent):
        if e.path:
            try:
                with open(e.path, "w", encoding=utf-8) as f:
                    f.write(text_area.value)
                    current_file_path["path"] = e.path
                    page.snack_bar = ft.SnackBar(ft.Text(f"Saved: {e.path}"))
                    page.snack_bar.open = True
                    page.update()
            except Exception as err:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error: {err}", color="red"))
                page.snack_bar.open = True
                page.update()

    def save_clicked(e):
        if current_file_path["path"]:
            try:
                with open(current_file_path["path"], "w", encoding="utf-8") as f:
                    f.write(text_area.value)
                    page.snack_bar = ft.SnackBar(ft.Text(f"Saved to: {current_file_path['path']}"))
                    page.snack_bar.open = True
                    page.update()
            except Exception as err:
                page.snack_bar = ft.SnackBar(ft.Text(f"Error: {err}", color="red"))
                page.snack_bar.open = True
                page.update()
        else:
            file_picker_save_as.save_file(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["txt"])

    file_picker_open.on_result = open_file_result
    file_picker_save_as.on_result = save_as_result

    page.overlay.append(file_picker_open)
    page.overlay.append(file_picker_save_as)
    page.add(
        text_area,
        ft.Row(
            [
                ft.ElevatedButton("Open", icon=ft.Icons.FOLDER_OPEN, on_click=lambda e: file_picker_open.pick_files(allow_multiple=False)),
                ft.ElevatedButton("Save", icon=ft.Icons.SAVE, on_click=save_clicked),
                ft.ElevatedButton(
                    "Save As",
                    icon=ft.Icons.SAVE_AS,
                    on_click=lambda e: file_picker_save_as.save_file(file_type=ft.FilePickerFileType.CUSTOM, allowed_extensions=["txt"])
                )
            ],spacing=10, alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
