# Major Project 1: Text Editor

This Flet application is a simple yet functional text editor.

## Features

- **Text Editing:** A large, multi-line text area allows for comfortable typing and editing.
- **Open File:** Users can open text files (`.txt`) from their local machine. The content of the file is loaded into the text area.
- **Save As:** Users can save the content of the text area to a new file. A file picker dialog is shown to choose the location and name of the new file.
- **Save:** If a file has been opened or previously saved, this option allows the user to quickly save any changes back to the same file. If no file is currently being edited, this behaves like "Save As".
- **Notifications:** The application uses `SnackBar` notifications to provide feedback on actions like opening or saving files, and to show any errors that occur.

## How it Works

1.  **UI Setup:**

    - The main UI consists of a large `TextField` (`text_area`) that expands to fill the available space.
    - Three `ElevatedButton` controls ("Open", "Save", "Save As") are placed at the bottom.

2.  **File Operations:**

    - **File Pickers:** The application uses two `FilePicker` instances: one for opening files (`file_picker_open`) and one for saving (`file_picker_save_as`). These are added to the page's `overlay`.
    - **`current_file_path`:** A dictionary is used to keep track of the path of the currently opened file. This is crucial for the "Save" functionality.

3.  **Core Functions:**

    - **`open_file_result(e)`:** This function is the callback for the open file picker. When a file is selected, it reads the file's content and populates the `text_area`. It also stores the file's path in `current_file_path`.
    - **`save_as_result(e)`:** This is the callback for the "Save As" file picker. It writes the content of the `text_area` to the path chosen by the user and updates `current_file_path`.
    - **`save_clicked(e)`:** This function handles the "Save" button click.
      - If `current_file_path` contains a path, it writes the text area content directly to that path.
      - If `current_file_path` is empty (i.e., it's a new document), it triggers the "Save As" file picker to prompt the user for a file location.

4.  **Error Handling:** All file operations are wrapped in `try...except` blocks to catch potential `IOError` or other exceptions. Errors are displayed to the user via the `SnackBar`.

simnpel text editor
