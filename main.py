from tkinter import font
import PySimpleGUI as sg
import os
import os.path
import urllib.request

# Functions

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def installIC():
    print('     Make the folder...')
    os.mkdir(pathiconicfolder)
    print('     Downloading jar...')
    urllib.request.urlretrieve(urljar, pathiconicfolder + '\Iconic-1.8.8.jar')
    print('     Downloading json...')
    urllib.request.urlretrieve(urljson, pathiconicfolder + '\Iconic-1.8.8.json')
    print('Done! You can now close this window.')

def updateIC():
    print('     Deleting existing files...')
    os.remove(pathiconicfolder + '\Iconic-1.8.8.jar')
    os.remove(pathiconicfolder + '\Iconic-1.8.8.json')
    print('     Downloading jar...')
    urllib.request.urlretrieve(urljar, pathiconicfolder + '\Iconic-1.8.8.jar')
    print('     Downloading json...')
    urllib.request.urlretrieve(urljson, pathiconicfolder + '\Iconic-1.8.8.json')
    print('Done! You can now close this window.')

# App Variables

path = os.getenv('APPDATA')
pathversions = path + '\.minecraft\\versions'
pathiconicfolder = pathversions + '\Iconic-1.8.8'
urljar = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.jar"
urljson = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.json"
changelogText = urllib.request.urlopen("https://download.iconicclient.tk/changelog.txt")
logoImage = resource_path("picture.png/picture.png")
iconImage = resource_path("icon.ico/icon.ico")

# pysimplegui Variables

sg.theme("Material2")
installerLayout = [
            [sg.Output(size=(50, 10), background_color='black', font='Consolas 8')],
            [sg.Button('Install', k='installBt')]]

updaterLayout = [
            [sg.Output(size=(50, 10), background_color='black', font='Consolas 8')],
            [sg.Button('Update', k='updateBt')]]

changelogLayout = [
            [sg.Text('', k='changelogElement')]
]

layout = [[sg.Image(logoImage, size=(75,75))],
          [sg.Text('Iconic Client Installer', font='Arial', k="test")],
          [sg.TabGroup([[sg.Tab('Install', installerLayout), sg.Tab('Update', updaterLayout), sg.Tab('Changelog', changelogLayout)]])]]

window = sg.Window('Iconic Client Installer', layout, margins=(50, 10), element_justification='c', icon=iconImage, finalize=True)

# Execute after gui open

def setText(Text):
    decodedText = Text.read().decode("utf-8")
    window['changelogElement'].update(value=decodedText)

setText(changelogText)

# While loop, listening for events 

while True:  
    event, values = window.read()

    if event in ('installBt', 'Install'):
        if str(os.path.isdir(pathversions)) == "True":
            print('Started installing Iconic Client 1.8.8')
            if str(os.path.isdir(pathiconicfolder)) == "False":
                installIC()
            else:
                print('Error Code 2: Folder exists. Did you mean to update?')
        else:
            print('Error Code 1: You might not have installed Minecraft. Contact us on our Discord server.')
    
    if event in ('updateBt', 'Update'):
        print('Updating Iconic Client.')
        if str(os.path.isdir(pathiconicfolder)) == "True":
            updateIC()
        else:
            print('Error Code 3: Folder does not exists. Did you mean to install?')      

    if event == sg.WIN_CLOSED:
        break


window.close()