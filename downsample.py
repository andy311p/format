from pydub import AudioSegment as am
import librosa
#important to [pip install librosa==0.7.2] version for librosa.output

output_dir = "/data/"

#open summary of files 
f = open(output_dir + "TRANS.txt",'r',encoding="utf8")
for line in f.readlines()[1:]:
    line = line.split()
    #construct json format
    curr_path = output_dir + line[1] + "/" + line[0]
  
    #####option 1
    sound = am.from_file(curr_path, format='wav', frame_rate=16000)
    sound = sound.set_frame_rate(8000)
    sound.export(curr_path, format='wav')
    
    ######option 2
    #if no sr is set, the default would be 22050
    y, s = librosa.load(curr_path, sr=8000)
    librosa.output.write_wav(curr_path, y, s)
