from tkinter import font
import PySimpleGUI as sg
import os, sys
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
changelogText = urllib.request.urlopen("https://download.iconicclient.tk/changelog.txt").read().decode("utf-8")
logoImage = resource_path("picture.png/picture.png")
iconImage = resource_path("icon.ico/icon.ico")
version = '2.1.0'
latest_version = urllib.request.urlopen("https://download.iconicclient.tk/installer-version.txt").read().decode("utf-8")

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

aboutLayout = [
            [sg.Text('Iconic Client Installer - ' + version)],
            [sg.Button('Check For Updates', k='UpdatesCheck')],
            [sg.Text('', k='versionStatus')]
]

layout = [[sg.Image(logoImage, size=(75,75))],
          [sg.Text('Iconic Client Installer', font='Arial', k="test")],
          [sg.TabGroup([[sg.Tab('Install', installerLayout), sg.Tab('Update', updaterLayout), sg.Tab('Changelog', changelogLayout), sg.Tab('About', aboutLayout, element_justification='c')]])]]

window = sg.Window('Iconic Client Installer', layout, margins=(50, 10), element_justification='c', icon=iconImage, finalize=True)

# Execute after gui open

def setText(Text):
    window['changelogElement'].update(value=changelogText)

setText(changelogText)

def checkForUpdates():
    if latest_version == version:
        window['versionStatus'].update(value='No updates needed.')
    else:
        window['versionStatus'].update(value='New version found: ' + latest_version + '\nPlease redownload the installer to apply the new update.')

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
    
    if event in ('UpdatesCheck', 'Check For Updates'):
        checkForUpdates()

    if event == sg.WIN_CLOSED:
        break


window.close()