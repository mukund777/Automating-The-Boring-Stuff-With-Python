# Pre-requisite : install webbrowser using pip command => pip install webbrowser
import webbrowser as wb

# 1. Opens the url in a new tab
wb.open('http://google.com')

# 2. Opens the url in a new tab. Same as 1
wb.open('http://google.com', new = 1)

# 3. Opens url in a new window. 
wb.open_new('http://google.com')

# 4. Opens url in a new tab. Same as 1 and 2
wb.open_new_tab('http://google.com')

# All urls are opened in the default browser. 
# Refer https://docs.python.org/3/library/webbrowser.html for official webbrowser documentation. 