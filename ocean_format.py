import tarfile
import os
import pathlib
import json
import wave
import contextlib


# with io.open(script_path + "/1110.txt", 'r', encoding='gb2312') as fn:
#   lines = fn.readlines()

# for fname in os.listdir(script_path):
#     blockSize = 1048576
#     with codecs.open(script_path + fname,"r",encoding="utf-16") as sourceFile:
#         with codecs.open(script_path + fname + "_","w",encoding="UTF-8") as targetFile:
#             while True:
#                 for i in sourceFile.readlines():
#                     a = i
#                 contents = sourceFile.read(blockSize)
#                 if not contents:
#                     break
#                 targetFile.write(contents)

script_path = str(pathlib.Path(__file__).parent.as_posix()) + '/ocean/Script/'
channel_path = str(pathlib.Path(__file__).parent.as_posix()) + '/ocean/Channel'

data = []
#run over all the files in the Script path
for fname in os.listdir(script_path):
    #codecs.encode(fname,encoding='utf-8', errors='strict')
    file = open(script_path + fname,'r',encoding="gb2312")
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
