# Imports
from pynput.keyboard import Key, Controller
from json import load
import keyboard

# Define Controller
kb = Controller()

# Define Hotkey Linking Function
def link(keys, output):
    # Define Function to Link to Hotkey
    def action():
        # Backspace through Hotkey
        for _ in range(len(keys)):
            kb.press(Key.backspace)
            kb.release(Key.backspace)
        
        # Write Output
        keyboard.write(output)

        # If Cursor Specification:
        if '$' in output:
            # Arrow Key to Cursor Specification
            for _ in range(len(output) - output.index('$') - 1):
                keyboard.press_and_release('left')
            
            # Remove $
            kb.press(Key.backspace)
            kb.release(Key.backspace)
    
    # Add Hotkey
    keyboard.add_hotkey('+'.join(list(keys)), action)

# Access database
database = load(open('Python.json', 'r'))

# Link Hotkeys
for keys, output in database.items():
    link(keys, output)

# Wait for Keyboard Action
keyboard.wait()