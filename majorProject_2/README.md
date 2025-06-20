# Major Project 2: Notes App with Database

This Flet application is a persistent notes-taking application that uses a SQLite database to store and manage notes.

## Features

- **Create Notes:** Users can add new notes with a title and content.
- **Persistent Storage:** Notes are saved to a `notes.db` SQLite database file, ensuring they are not lost when the app is closed.
- **View Notes:** All saved notes are displayed in a clean, scrollable list of cards.
- **Delete Notes:** Each note has a delete button to remove it from the database.
- **Simple Interface:** A straightforward layout with input fields, an "Add" button, and a display area for notes.

## How it Works

The project is split into two main files: `main.py` for the user interface and `db.py` for database interactions.

### `db.py`: Database Management

This file contains all the functions for interacting with the SQLite database.

- **`init_db()`**: Creates a `notes.db` file if one doesn't exist and sets up the `notes` table with `id`, `title`, and `content` columns.
- **`add_note(title, content)`**: Inserts a new record into the `notes` table.
- **`get_notes()`**: Fetches all records from the `notes` table.
- **`delete_note(note_id)`**: Deletes a record from the `notes` table based on its unique `id`.

### `main.py`: User Interface (Flet)

This file builds the application's front-end and handles user interactions.

1.  **Initialization:**
    - `init_db()` is called on startup to ensure the database is ready.
    - `load_notes()` is called to fetch and display any existing notes.
2.  **Adding a Note (`add_note_clicked`)**:
    - When the "Add Note" button is clicked, it takes the values from the `title_input` and `content_input` fields.
    - It calls the `add_note` function from `db.py` to save the new note.
    - The input fields are cleared.
    - `load_notes()` is called again to refresh the list of displayed notes.
3.  **Displaying Notes (`load_notes`)**:
    - This function first clears the current list of notes in the UI.
    - It calls `get_notes()` from `db.py` to retrieve all notes.
    - It then iterates through the notes, creating a `ft.Card` for each one, and adds it to the `notes_column`. Each card includes a delete `IconButton`.
4.  **Deleting a Note (`delete_note_and_refresh`)**:
    - The delete button on each card is linked to this function, passing the specific `note_id`.
    - It calls `delete_note(note_id)` from `db.py` to remove the note from the database.
    - It then calls `load_notes()` to update the UI, removing the deleted note's card.
