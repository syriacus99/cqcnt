import subprocess
import os
commend_1 = os.walk("./")
file_names = list()

for a,b,file_names in commend_1:
    pass

if file_names:
    for file_name in file_names:
        if file_name.split(".")[1] == 'mp4':
            do_command = subprocess.call("/usr/local/ffmpeg/bin/ffmpeg -i "+'"'+file_name+ '"'+" -f image2 -frames:v 1 " +'"'+file_name.split(".")[0]+'"'+".jpg",
                                        shell=True)