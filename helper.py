import os


def filelist(folder_key, values, window):
    """Update filelist"""
    values = values
    window = window
    folder = values[folder_key]
    try:
        # try to get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".png", ".gif"))
    ]
    return file_list, fnames
