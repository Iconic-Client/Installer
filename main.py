import os
import os.path
import wget
from os import path

path = os.getenv('APPDATA')
pathversions = path + '\.minecraft\\versions'
pathiconicfolder = pathversions + '\Iconic-1.8.8'
urljar = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.jar"
urljson = "https://iconicdownloadproxy.netlify.app/Iconic-1.8.8.json"

print ("Checking if Minecraft versions folder exists: " + str(os.path.isdir(pathversions)))
if str(os.path.isdir(pathversions)) == "True":
    print("Downloading Iconic Client 1.8.8")
    print(' Make the folder...')
    os.mkdir(pathiconicfolder)
    print(' Downloading jar...')
    wget.download(urljar, pathiconicfolder + '\Iconic-1.8.8.jar')
    print('\n Downloading json...')
    wget.download(urljson, pathiconicfolder + '\Iconic-1.8.8.json')
    print('\n Done!')
    exit()
else:
    print("Make sure you have installed Minecraft.")
    exit()