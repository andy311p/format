import tarfile
import os
import pathlib
import json
import wave
import contextlib

dir_name = "/out" #enter desired output dir name

output_dir = str(pathlib.Path(__file__).parent.as_posix()) + dir_name

#first time data is extracted
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
    with tarfile.open(str(pathlib.Path(__file__).parent.absolute()) + "/test_set.tar.gz", "r") as archive:
        archive.extractall(output_dir)

#open summary of files 
data = []
f = open(output_dir + "/test/TRANS.txt",'r',encoding="utf8")
for line in f.readlines()[1:]:
    line = line.split()
    #construct json format
    curr_path = dir_name + "/test/" + line[1] + "/" + line[0]
    
    #get the duration of the .WAV file
    with contextlib.closing(wave.open("./" + curr_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    
    data.append({
        "audio_filepath": curr_path,
        "duration": duration,
        "text": line[2]
        })
f.close()


#print the data in the right format
with open('output.txt', 'w',encoding="utf-8") as outfile:
    for i in data:
        json.dump(i, outfile,ensure_ascii=False)
        outfile.write('\n')
