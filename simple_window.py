# make a simple app to display images
# if possible, make it an app to sort images

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
import os.path

# layout (text to be displayed and buttons)
layout = [
    [sg.Text("Image Sorting")],
    [sg.Button("Positive")],
    [sg.Button("Negative")],
    [sg.Button("Ciao")],
]

window = sg.Window("Image Sorter", layout, margins=(100, 50))

# .read() to display
# window.read()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button # WIN_CLOSED is x button in corner
    if event == "Ciao" or event == sg.WIN_CLOSED:
        break

window.close()
