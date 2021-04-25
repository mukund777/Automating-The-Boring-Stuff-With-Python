# Pre-requisites : install xsel, xclip, gtk, PyQt4, pyperclip modules using pip => pip install "module name"
import pyperclip as pc

# Copies data to the clipboard. Works only in the program and cannot be pasted into some ide or other places. 
pc.copy("Some Text")

# Pastes the clipboard contents and displays it on the terminal.
print(pc.paste())

# Blocks and doesn’t return until a non-empty text string is on the clipboard.
pc.waitForPaste()

# Blocks until the text on the clipboard has changed
pc.waitForNewPaste()

# Refer https://pyperclip.readthedocs.io/en/latest/ for pyperclip documentation. 

