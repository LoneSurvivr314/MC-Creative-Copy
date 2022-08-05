import nbtlib

file = nbtlib.load(r"C:\Users\TAK\AppData\Roaming\.minecraft\saves\Good World\level.dat")
print(file["Data"]["Player"]["playerGameType"])
