from hashlib import new
from time import time
import nbtlib
from nbtlib.tag import Int, Byte, String
import shutil
from pathlib import Path
from datetime import datetime

def backup(worldFolder, backupFolder):
    """
    Backs up a minecraft world to another folder
    
    Parameters
    ---
    worldFolder: a string or Path object
        The folder containing the world to back up
    backupFolder: a string or Path object
        The folder to which you want the backup to be saved. Note that this function creates a folder containing the world folder
    """
    
    # Initialize path objects
    worldFolder = Path(worldFolder)
    backupFolder = Path(backupFolder)
    # get the current time and format it
    fTime = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    print(worldFolder,backupFolder/fTime)
    # Copy the world folder,adding the original game folder back
    shutil.copytree(worldFolder,backupFolder/fTime/worldFolder.stem)

def creativeCopy(worldFolder, newLocation):
    """
    Creates a copy of a world in creative mode and cheats enabled
    
    Parameters
    ---
    worldFolder: a string or Path object
        The folder containing the world to back up
    newLocation: a string or Path object
        The folder where the world will be copied to.
    """
    
    # Initialize path objects
    worldFolder = Path(worldFolder)
    newLocation = Path(newLocation)/(worldFolder.stem+"- Creative Copy") # create the new fold with the smae name as the old, appending " - Creative Copy"
    # Copy the world folder
    shutil.copytree(worldFolder,newLocation)
    

    with nbtlib.load(newLocation/"level.dat") as file:
        file["Data"]["Player"]["playerGameType"] = Int(1)
        file["Data"]["GameType"] = Int(1)
        file["Data"]["allowCommands"] = Byte(1)
        file["Data"]["LevelName"] = String(file["Data"]["LevelName"] + " - Creative Copy")
    
    with nbtlib.load(newLocation/"level.dat_old") as file:
        file["Data"]["Player"]["playerGameType"] = Int(1)
        file["Data"]["GameType"] = Int(1)
        file["Data"]["allowCommands"] = Byte(1)
        file["Data"]["LevelName"] = String(file["Data"]["LevelName"] + " - Creative Copy")
        
#backup(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World",r"C:\Users\TAK\Desktop\Backup\MC")
creativeCopy(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World",r"C:\Users\TAK\AppData\Roaming\.minecraft\saves")