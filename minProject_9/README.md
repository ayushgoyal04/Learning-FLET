# Mini Project 9: Image Viewer

This Flet application allows users to select a local image file and display it within the application window.

## Features

- **File Selection:** A "Select Image" button opens a native file picker dialog for the user to choose an image.
- **Image Preview:** The selected image is displayed in a preview area.
- **File Information:** The name of the loaded image file is shown.
- **Single File Support:** The file picker is configured to allow only one file to be selected at a time.

## How it Works

1.  **FilePicker:** The application uses Flet's `FilePicker` control to handle file selection. This control is added to the page's `overlay` so it can be shown on top of other content.
2.  **Button Click:** The "Select Image" button's `on_click` event calls the `file_picker.pick_files()` method. This opens the system's file dialog.
3.  **Handling the Result (`on_file` function):**
    - The `FilePicker`'s `on_result` property is set to the `on_file` function, which is called after the user selects a file (or cancels).
    - If files were selected (`e.files` is not empty), the `src` property of the `Image` control (`image_preview`) is set to the path of the first selected file (`e.files[0].path`).
    - A `Text` control (`info_text`) is updated to show the name of the selected file.
    - If no file was selected, the image source is cleared, and the info text is updated accordingly.
4.  **UI Updates:** `image_preview.update()` and `info_text.update()` are called to refresh the UI and display the new image and text.

## How to Run

1. Install requirements:
   ```bash
   pip install flet
   ```
2. Run the app:
   ```bash
   python main.py
   ```

## File Structure

- `main.py` - Main Flet app

---

Enjoy viewing your images easily!
