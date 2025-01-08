import os
import shutil
directory = os.path.join(os.path.expanduser("~"), "Downloads")
types = {  
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".jpeg": "Images",
    ".HEIC": "Images",
    ".webp": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Docs",
    ".pdf": "Docs",
    ".txt": "Docs",
    ".docx": "Docs",
    ".mp3": "Music",
    ".wav": "Music",
    ".jar": "Minecraft",
    ".dmg": "Apps",
    ".csv": "Data",
    ".json": "Data",
    ".zip": "ZIP Files"

}
for fileName in os.listdir(directory):
    
    filePath = os.path.join(directory, fileName)
    
    if os.path.isfile(filePath):
        fileType = os.path.splitext(fileName)[1].lower()
        if fileType in types:
            folder = os.path.join(directory, types[fileType])
            os.makedirs(folder, exist_ok = True)
            destination = os.path.join(folder, fileName)
            shutil.move(filePath, destination)
            print(f"moved {fileName} to {types[fileType]}")
        else:
            print(f"skipped {fileName}, unknown file type")

    else:
        pass


