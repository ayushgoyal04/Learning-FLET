import flet as ft

def main(page: ft.Page):
    page.title = "Image Viewer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    image_preview = ft.Image(width=400, height=400, fit=ft.ImageFit.CONTAIN)
    info_text = ft.Text("Select an image to preview.", size=16)

    def on_file(e):
        if e.files:
            image_preview.src = e.files[0].path
            info_text.value = f"Loaded: {e.files[0].name}"
        else:
            image_preview.src = None
            info_text.value = "No image selected."
        image_preview.update()
        info_text.update()

    file_picker = ft.FilePicker(on_result=on_file)

    select_btn = ft.ElevatedButton("Select Image", on_click=lambda _: file_picker.pick_files(allow_multiple=False))

    page.add(
        ft.Column([
            info_text,
            select_btn,
            image_preview,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        file_picker
    )

ft.app(target=main)
