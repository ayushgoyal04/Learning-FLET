# Mini Project 3: Digital Clock

This Flet application displays a live digital clock that updates every second.

## Features

- **Real-time Clock:** The application shows the current time in HH:MM:SS format.
- **Live Updates:** The time is updated every second without needing any user interaction.
- **Custom Styling:** The clock display uses a large font size, a cyan color, and bold weight for better visibility.

## How it Works

The application UI consists of a single `Text` control to display the time.

A separate thread is started using `page.run_thread(update_clock)` to handle the time updates. The `update_clock` function runs in an infinite loop (`while True`).

Inside the loop:

1.  `datetime.datetime.now().strftime("%H:%M:%S")` gets the current time formatted as hours, minutes, and seconds.
2.  The `value` of the `Text` control (`time_display`) is updated with the new time string.
3.  `page.update()` is called to refresh the UI and show the new time.
4.  `time.sleep(1)` pauses the loop for one second, ensuring the clock updates every second.

This approach of using a separate thread is crucial for preventing the UI from freezing while waiting for time updates.
