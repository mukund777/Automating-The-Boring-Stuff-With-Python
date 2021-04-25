import webbrowser as wb
import sys
import pyperclip

if len(sys.argv) > 1 : 
	address = ' '.join(sys.argv[1:])
else : 
	address = pyperclip.paste()

wb.open('https://www.google.com/maps/place/' + address)

