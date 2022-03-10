from fileinput import close
from tkinter import font
import PySimpleGUI as sg
import os
import os.path
import urllib.request

path = os.getenv('APPDATA')
pathversions = path + '\.minecraft\\versions'
pathiconicfolder = pathversions + '\Iconic-1.8.8'
urljar = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.jar"
urljson = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.json"
popupContent = urllib.request.urlopen("https://download.iconicclient.tk/changelog.txt")


sg.theme("Material2")
layout = [[sg.Image(r'C:\\Users\sidcd\Downloads\\IconicClient-Installer\\picture.png',size=(75,75))],
          [sg.Text('Installing Iconic Client', font='Arial', k="test")],
          [sg.Output(size=(50, 10), background_color='black', font='Consolas 8')],
          [sg.Button('Install')],
          [sg.Button('Changelog')]]
window = sg.Window('Iconic Client Installer', layout, margins=(200, 200), element_justification='c', icon=r'C:\\Users\sidcd\Downloads\\IconicClient-Installer\\icon.ico')

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

    if event in (None, 'Changelog'):
        for line in popupContent:
            decoded_line = line.decode("utf-8")
            print(decoded_line)

    if event == sg.WIN_CLOSED:
        break
window.close()