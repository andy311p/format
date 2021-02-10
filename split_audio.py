import librosa
import os
from datetime import datetime

#input is folder with files XX_1.wav and XX_1.srt files
input = "input/"
#output is metadata.csv and splitted files
output = "output/"

out_f = open(output + "metadata.csv","w")

zero_time = datetime.strptime("00:00:00,000","%H:%M:%S,%f")
print("start Process")
for file in os.listdir(input):
    if file[-3:] == "wav":
        print("Proccessing file: {}".format(file_name))
        file_name = file[:-4]
        subfile_id = 1
        try:
            transcript = open(input + file_name + ".srt","r")
        except:
            print("ERROR: no transcript for file {}".format(file_name))
            pass
        try:
            audio, sr = librosa.load(input + file)
        except:
            print("ERROR: loading wav file {}".format(file_name))
            pass
        
        step = 0
        for line in transcript.readlines():
            line = line.split()
            if line:
                #id
                if step == 0:
                    step += 1
                #time interval
                elif step == 1:
                    step += 1
                    start = (datetime.strptime(line[0],"%H:%M:%S,%f") - zero_time).total_seconds() 
                    end = (datetime.strptime(line[2],"%H:%M:%S,%f") - zero_time).total_seconds()                    
                #text
                else:
                    step = 0
                    chunk = audio[int(start * sr) : int(end * sr)]
                    librosa.output.write_wav(output + "wavs/" +  file_name + "_" +  str(subfile_id).zfill(5) + ".wav", chunk, sr)
                    out_f.write("{}|{}|{}\n".format(file_name + "_" +  str(subfile_id).zfill(5), " ".join(line), " ".join(line) ))
                    subfile_id += 1
print("END Process")
