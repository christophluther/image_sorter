# a simple app to display and sort images

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED, Window
import os.path
import shutil
from helper import filelist

file_list_column = [
    [
        sg.Text("Image Folder"),
        # In is for input
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 50), key="-FILE LIST-"
        )
    ],
]

# for now: only show file name of chosen file instead of image
image_viewer_column = [
    [sg.Text("Choose image from list on left:")],
    [sg.Text(size=(60, 1), key="-TOUT1-")],
    [sg.Text(size=(60, 1), key="-TOUT2-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Positive"), sg.Button("Neutral"), sg.Button("Negative")],
]

# now the layout that you pass into the window

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        file_list, fnames = filelist("-FOLDER-", values, window)
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":
        # i.e. file was chosen from file list (clicked = event)
        filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
        basename = os.path.basename(filename)
        window["-TOUT1-"].update(filename)
        window["-TOUT2-"].update(basename)
        window["-IMAGE-"].update(filename=filename)

    else:
        pass

    if event == "Positive":
        move_to = f"Positive/{basename}"
        shutil.move(str(filename), move_to)
        file_list, fnames = filelist("-FOLDER-", values, window)
        window["-FILE LIST-"].update(fnames)
        if len(fnames) > 0:
            # i.e. file was chosen from file list (clicked = event)
            filename = str(values["-FOLDER-"] + "/" + fnames[0])
            basename = os.path.basename(filename)
            window["-TOUT1-"].update(filename)
            window["-TOUT2-"].update(basename)
            window["-IMAGE-"].update(filename=filename)

    elif event == "Neutral":
        move_to = f"Neutral/{basename}"
        shutil.move(str(filename), move_to)
        file_list, fnames = filelist("-FOLDER-", values, window)
        window["-FILE LIST-"].update(fnames)
        if len(fnames) > 0:
            # i.e. file was chosen from file list (clicked = event)
            filename = str(values["-FOLDER-"] + "/" + fnames[0])
            basename = os.path.basename(filename)
            window["-TOUT1-"].update(filename)
            window["-TOUT2-"].update(basename)
            window["-IMAGE-"].update(filename=filename)

    elif event == "Negative":
        move_to = f"Negative/{basename}"
        shutil.move(str(filename), move_to)
        file_list, fnames = filelist("-FOLDER-", values, window)
        window["-FILE LIST-"].update(fnames)
        if len(fnames) > 0:
            # i.e. file was chosen from file list (clicked = event)
            filename = str(values["-FOLDER-"] + "/" + fnames[0])
            basename = os.path.basename(filename)
            window["-TOUT1-"].update(filename)
            window["-TOUT2-"].update(basename)
            window["-IMAGE-"].update(filename=filename)


window.close()
