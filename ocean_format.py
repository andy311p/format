import tarfile
import os
import pathlib
import json
import wave
import contextlib

script_path = str(pathlib.Path(__file__).parent.as_posix()) + '/ocean/Script/'
channel_path = str(pathlib.Path(__file__).parent.as_posix()) + '/ocean/Channel'

data = []
#run over all the files in the Script path
for fname in os.listdir(script_path):
    file = open(script_path + fname,'r',encoding="utf8")
    for i,line in enumerate(file.readlines()[0:2]):
        if i % 2 == 0:
            line = line.split()
            for j in range(1,5):
                #get the duration of the .WAV file
                curr_path = channel_path + str(j) + "/" + line[0][0:4] + "/" + line[0] + ".wav"
                with contextlib.closing(wave.open(curr_path,'r')) as f:
                    frames = f.getnframes()
                    rate = f.getframerate()
                    duration = frames / float(rate)
                data.append({
                    "audio_filepath": curr_path,
                    "duration": duration,
                    "text": line[1]
                    })
    file.close()    
    
#print the data in the right format
with open('output.txt', 'w',encoding="utf-8") as outfile:
    for i in data:
        json.dump(i, outfile,ensure_ascii=False)
        outfile.write('\n')

