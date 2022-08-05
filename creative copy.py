import nbtlib
from nbtlib.tag import Int, Byte, String
import shutil
from pathlib import Path

def backup(worldFolder, backupFolder):
    worldFolder = Path(worldFolder)
    backupFolder = Path(backupFolder)
    
    shutil.copytree(worldFolder,backupFolder/)

with nbtlib.load(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World\level.dat") as file:
    file["Data"]["Player"]["playerGameType"] = Int(1)
    file["Data"]["GameType"] = Int(1)
    file["Data"]["allowCommands"] = Byte(1)

with nbtlib.load(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World\level.dat_old") as file2:
    file2["Data"]["Player"]["playerGameType"] = Int(1)
    file2["Data"]["GameType"] = Int(1)
    file2["Data"]["allowCommands"] = Byte(1)