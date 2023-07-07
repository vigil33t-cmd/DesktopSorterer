import os
import subprocess
import logging
import shutil
from extensions import Folders
blacklist = [folder for folder in Folders]
desktop = subprocess.check_output(["powershell", "-C", "[Environment]::GetFolderPath([Environment+SpecialFolder]::Desktop)"]).decode().replace('\r\n','')

filesOnDesktop = os.listdir(desktop)

def getTypeOfFileByExtension(filePath):
    fileName = filePath.split('\\')[-1]
    fileExtension = fileName.split('.')[-1]
    for folder in Folders:
        if fileExtension in Folders[folder]['Extensions']:
            return {
                    "fileName": fileName,
                    "fileExtension": fileExtension,
                    "folder": folder
                    }
        
        
for folder in [folder for folder in Folders]:
    if not os.path.exists(f'{desktop}\\{folder}'):
        os.mkdir(f'{desktop}\\{folder}')

for file in filesOnDesktop:
    dist = f"{desktop}\\{file}"
    if not os.path.isdir(dist):
        folder = getTypeOfFileByExtension(dist)
        if folder != None:
            shutil.move(dist, f"{desktop}\\{folder['folder']}")
    if file not in blacklist:
        shutil.move(dist, f"{desktop}\\Folders")
        
        