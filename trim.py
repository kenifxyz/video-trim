import os
import subprocess
import pathlib
import time
dir = str(pathlib.Path(__file__).parent.resolve())
dir = dir.replace(" ", "\ ")
files = os.listdir(".")
untrimmedFiles = []
trimmedFiles = []
totalFiles = 0
currentFile = 0
for f in files:
    if "t-" in f:
        trimmedFiles.append(f[2:])

for f in files:
    if f in trimmedFiles or 't-' in f:
        continue
    else:
        untrimmedFiles.append(f)

for f in untrimmedFiles:
    if f.endswith(".mp4"):
        totalFiles += 1
        
print("Total files: " + str(totalFiles))
for f in untrimmedFiles:
    currentFile += 1
    print("Trimming file " + str(currentFile) + " of " + str(totalFiles))
    if f.endswith(".mp4"):
        fileName = f.replace(" ", "\ ")
        absolutePath = dir + "/" + fileName
        outPath = dir + "/t-" + fileName
        command = "ffmpeg -ss 00:00:03.2 -i " + absolutePath + " -c copy " + outPath
        subprocess.run(command, shell=True)
        # remove original file
        try:
            time.sleep(0.3)
            absolutePath = absolutePath.replace("\ ", " ")
            os.remove(absolutePath)
        except:
            print("Could not remove " + absolutePath)
            pass