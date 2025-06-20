# Major Project 3: Flet Application Template

## Project Overview

This project serves as a template for creating a distributable Flet application. It includes the necessary file structure (`pyproject.toml`, `src` directory) and a comprehensive guide for running, building, and packaging your Flet app for multiple platforms including Android, iOS, and desktop (Windows, macOS, Linux).

### Example Application: Counter

The initial application provided in this template is a simple counter. It demonstrates basic Flet concepts:

- **State Management:** A number is stored as state and incremented.
- **Controls:** It uses `ft.Text` to display the count and a `ft.FloatingActionButton` to increment it.
- **Layout:** The counter is centered on the page using `ft.SafeArea` and `ft.Container`.

This simple example can be replaced with your own application logic in `src/main.py`.

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).
