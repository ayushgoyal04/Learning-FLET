import flet as ft
from db import init_db, add_note, get_notes, delete_note

def main(page: ft.Page):
    page.title = "Notes App"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    init_db()

    title_input = ft.TextField(label="Title", width=300)
    content_input = ft.TextField(label="Content", width=300, multiline=True, height=100, max_length=500)
    notes_column = ft.Column()

    def load_notes():
        notes_column.controls.clear()
        for note in get_notes():
            notes_column.controls.append(
                ft.Card(
                    content=ft.ListTile(
                        title=ft.Text(note[1]),
                        subtitle=ft.Text(note[2]),
                        trailing=ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            on_click=lambda e, note_id=note[0]: delete_note_and_refresh(note_id)
                        )
                    )
                )
            )
        page.update()

    def delete_note_and_refresh(note_id):
        delete_note(note_id)
        load_notes()


    def add_note_clicked(e):
        if title_input.value and content_input.value:
            add_note(title_input.value, content_input.value)
            title_input.value = ""
            content_input.value = ""
            load_notes()



    page.add(
        title_input,
        content_input,
        ft.ElevatedButton("Add Note", on_click=add_note_clicked),
        ft.Divider(),
        ft.Text("Saved notes: ", size=20, weight="w500"),
        notes_column
    )

ft.app(target=main)
