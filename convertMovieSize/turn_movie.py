import os
import subprocess

import json
def getSize(file_name):
    command = 'ffprobe -select_streams v -show_entries format=duration,size,bit_rate,filename -show_streams -v quiet -of csv="p=0" -of json -i ' +file_name
    result = subprocess.Popen(command,shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    out = result.stdout.read()
    data ={"width":0,"height":0,'duration':0}
    temp = str(out.decode('utf-8'))
    try:
        data["width"] = json.loads(temp)['streams'][0]['width']
        data["height"] = json.loads(temp)['streams'][0]['height']
        data["duration"] = json.loads(temp)['format']['duration']
    except:
        data["width"] = json.loads(temp)['streams'][1]['width']
        data["height"] = json.loads(temp)['streams'][1]['height']
        data["duration"] = json.loads(temp)['format']['duration']
    return data


def transform_movie(size,file_name):
    print(size)
    if size['height']*16//9 % 2 != 0:
        new_width = size['height']*16//9 +1
    else:
        new_width = size['height']*16//9
    command = 'ffmpeg -i '+file_name+' -vf "split[a][b];[a]scale='+str(new_width)+':'+str(size['height'])+',boxblur=10:5[1];[b]scale='+str(size['width'])+':'+str(size['height'])+'[2];[1][2]overlay=(W-w)/2:0" -c:v libx264 -crf 18 -aspect 16:9  -f mp4 '+'t_'+file_name+' -y'
    #command = '/usr/local/ffmpeg/bin/ffmpeg -y -f lavfi -i color=LightCyan:'+str(size['height']*16//9)+'x'+str(size['height'])+':d='+str(size['duration'])+' -format rgb32 -f matroska  black.mp4'
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.stdout.read()
    print(out)

def main():
    commend_1 = os.walk("./")
    file_names = list()
    for a,b,file_names in commend_1:
        #print(file_names)
        pass

    if file_names:
        for file_name in file_names:
            if file_name.split(".")[-1] == 'mp4':
                size = getSize(file_name)
                transform_movie(size,file_name)
                
main()
#-hwaccel cuda
#'ffmpeg -hwaccel cuda -i 1.mp4 -vf "split[a][b];[a]scale=2276:1280,boxblur=10:5[1];[b]scale=720:1280[2];[1][2]overlay=(W-w)/2:0"  -c:v hevc_nvenc -crf 18 -f mp4 scale=1920:1080 out.mp4 -y'