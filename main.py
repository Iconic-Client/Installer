from fileinput import close
from tkinter import font
import PySimpleGUI as sg
import os
import os.path
import urllib.request

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pathversions = '~/Library/Application support/minecraft/versions/'
pathiconicfolder = pathversions + '/Iconic-1.8.8'
urljar = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.jar"
urljson = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.json"
popupContent = urllib.request.urlopen("https://download.iconicclient.tk/changelog.txt")
logoImage = resource_path("picture.png/picture.png")
iconImage = resource_path("icon.ico/icon.ico")

sg.theme("Material2")
layout = [[sg.Image(logoImage, size=(75,75))],
          [sg.Text('Installing Iconic Client', font='Arial')],
          [sg.Output(size=(50, 10), background_color='black', font='Consolas 8')],
          [sg.Button('Install')]]
window = sg.Window('Iconic Client Installer', layout, margins=(200, 200), element_justification='c', icon=iconImage, finalize=True)

def printAfter(Text):
    for line in Text:
        decodedText = line.decode("utf-8")
        print(decodedText)

printAfter(popupContent)

while True:  
    event, values = window.read()
    
    if event in (None, 'Install'):
        if str(os.path.isdir(pathversions)) == "True":
            print('Started installing Iconic Client 1.8.8')
            if str(os.path.isdir(pathiconicfolder)) == "False":
                print('     Make the folder...')
                os.mkdir(pathiconicfolder)
                print('     Downloading jar...')
                urllib.request.urlretrieve(urljar, pathiconicfolder + '\Iconic-1.8.8.jar')
                print('     Downloading json...')
                urllib.request.urlretrieve(urljson, pathiconicfolder + '\Iconic-1.8.8.json')
                print('Done! You can now close this window.')
            else:
                print('     Downloading jar...')
                urllib.request.urlretrieve(urljar, pathiconicfolder + '\Iconic-1.8.8.jar')
                print('     Downloading json...')
                urllib.request.urlretrieve(urljson, pathiconicfolder + '\Iconic-1.8.8.json')
                print('Done! You can now close this window.')
        else:
            print('Error Code 1: You might not have installed Minecraft. Contact us on our Discord server.')
          
    if event == sg.WIN_CLOSED:
        break
        
window.close()
