from unittest.mock import patch
from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input("Paste or type the link of the video you want to download: ")
path = input("Choose the directory you want to save the file: ")
yt = YouTube(link)


#Mostra os detalhes do video
print("Título: ", yt.title)
print("Número de views: ",yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")


#Baixa mp3
print("Downloading...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download complete!")


#Converte mp4 para mp3
print("converting file...")
for file in os.listdir(path):
    if re.search("mp4", file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+".mp3")
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucess!")


