import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe",
    
    'discord': "C:\\Users\\hegde\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

