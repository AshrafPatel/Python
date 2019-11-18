from sys import argv
import os
from PIL import Image
from pathlib import Path

def checkWorkDirExist():
    """Check if WorkDir Path exists if it does return True otherwise return False"""
    try:
        work_dir = Path(f"{os.getcwd()}/{argv[1]}")
        exist = os.path.isdir(work_dir)
        if exist:
            print("Working Directory found")
            return True
        print("Working Directory not found")
        return False
    except Exception as err:
        print("Error check your arguments!", err)
        return False


def checkNewDirectoryExists():
    """Check if NewDir for images Path exists if it does return True otherwise return False"""
    try:
        new_dir = Path(f"{os.getcwd()}/{argv[2]}")
        exist = os.path.isdir(new_dir)
        if exist:
            print("Folder for PNG images exists")
            return True
        print("Folder for PNG images not found... \nCreating Folder...")
        return False
    except Exception as err:
        print("Error check your arguments!", err)
        return False

def startConversion():
    """This function will convert JPG images to PNG"""
    if (checkWorkDirExist() and checkNewDirectoryExists()):
        work_dir = str(Path(f"{os.getcwd()}/{argv[1]}"))
        new_dir = str(Path(f"{os.getcwd()}/{argv[2]}"))
        for file in os.listdir(work_dir):
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                current_file_path = str(Path(work_dir + "/" + file))
                img = Image.open(current_file_path)
                filename = os.path.splitext(file)[0]
                img.save(f"{new_dir}/{filename}.png", "png")
        print("operation completed")
    elif (checkWorkDirExist() and not checkNewDirectoryExists()):
        os.makedirs(argv[2])
        startConversion()
    else:
        print("Could not run program. Please try again\nIs your working directory valid?\nCheck arguments provided")

startConversion()