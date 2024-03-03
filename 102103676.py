import sys
import urllib.request
import re
import pandas as pd
import random
from pytube import YouTube
from pydub import AudioSegment
import os
def mashup():
    X = sys.argv[1]                                    #Singer Name
    N = int(sys.argv[2])                               #Number of Videos
    Y = int(sys.argv[3])                               #Number of seconds to be trimmed
    X=X.lower()
    X=X.replace(" ", "")+"videosongs"
    html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+X)
    video_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())
    l=len(video_ids)
    url = []
    for i in range(N):
       url.append("https://www.youtube.com/watch?v=" + video_ids[random.randint(0,l-1)])
    final_aud = AudioSegment.empty()
    for i in range(N):   
      audio = YouTube(url[i]).streams.filter(only_audio=True).first()
      audio.download(filename='Audio-'+str(i)+'.mp3')
      print("\nAudio-"+str(i)+" Downloaded successfully✅")
      aud_file = str(os.getcwd()) + "/Audio-"+str(i)+".mp3"
      file1 = AudioSegment.from_file(aud_file)
      extracted_file = file1[:Y*1000]
      final_aud +=extracted_file
      final_aud.export(sys.argv[4], format="mp3")

    print("\nMashup Created Successfully")
def checkInputRequirements():
    if  len(sys.argv)==5:
        singername=sys.argv[1]
        NumberOfVids=int(sys.argv[2])
        MinAudioLength=int(sys.argv[3])
        if NumberOfVids<10:
            print("Number of videos must be 10 or more.")
            return
        if MinAudioLength<20:
            print("Audio length must be 20 or more")
            return
        resultFileName = sys.argv[-1].lower()
        if ".mp3" not in resultFileName:
            print("Final file must be in format of '.mp3'")
            return
        mashup()

    else :
        print("Provide 4 arguments along with the name of the code file")
        return
checkInputRequirements()