import os
from tqdm import tqdm
import json
import wave
import contextlib
path = "C:/Users/GH4866/WORK/MANDARIN/data_thchs30/data"

data = []
for i,fname in enumerate(tqdm(os.listdir(path)[1:])):
    curr_path = path + "/" + fname
    if i%2 == 0:
        audio_filepath = curr_path
        with contextlib.closing(wave.open(curr_path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
    else:
        text = open(curr_path,"r",encoding="UTF-8").readline().rstrip()
        data.append({
            "audio_filepath": audio_filepath,
            "duration": duration,
            "text": text
            })        
        
#print the data in the right format
with open('output.json', 'w',encoding="utf-8") as outfile:
    for i in data:
        json.dump(i, outfile,ensure_ascii=False)
        outfile.write('\n')