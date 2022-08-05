from time import time
import nbtlib
from nbtlib.tag import Int, Byte, String
import shutil
from pathlib import Path
from datetime import datetime

def backup(worldFolder, backupFolder):
    # Initialize path objects
    worldFolder = Path(worldFolder)
    backupFolder = Path(backupFolder)
    # get the current time and format it
    fTime = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    print(worldFolder,backupFolder/fTime)
    # Copy the folder
    shutil.copytree(worldFolder,backupFolder/fTime)


#with nbtlib.load(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World\level.dat") as file:
#    file["Data"]["Player"]["playerGameType"] = Int(1)
#    file["Data"]["GameType"] = Int(1)
#    file["Data"]["allowCommands"] = Byte(1)
#
#with nbtlib.load(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World\level.dat_old") as file2:
#    file2["Data"]["Player"]["playerGameType"] = Int(1)
#    file2["Data"]["GameType"] = Int(1)
#    file2["Data"]["allowCommands"] = Byte(1)

backup(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World",r"C:\Users\TAK\Desktop\Backup\MC")