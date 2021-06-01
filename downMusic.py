# File Name: downMusic.py
# Author: Antonio Yves de Sousa Dantas 
# Created on: May 31, 2021
# Last Modified on: June 01, 2021 at 02:19 PM
# License: MIT

'''
    to run this file you will need to install the library pytube

    for python3 use
    pip3 install pytube

    for python2 use
    pip install pytube

    if you just have one version of python in your computer, you just need to run the command
    pip install pytube

    hope you enjoy!
    
    feel free to make your own changes in the code and adapt for your real propose
'''

from pytube import YouTube, Playlist

'''
  Itag refs
  18 - video 360p
  22 - video 720p
  137 - video 1080p
  140 - music mp4 128kbps
'''


def downloadPlaylist(playlist:Playlist):
    '''
        this function download a playlist of videos from youtube as mp4 (as audio)
        only the audio of the video is downloaded, then if you want to download
        the video you need to change the itag on line 44
    '''
    for video in playlist:
        yt_video = YouTube(video)
        print(f"Downloading - {yt_video.title}\nPlease wait...")
        yt_video.streams.get_by_itag(140).download(f"musics/{playlist.title}")
    print("Download completed, enjoy!")

def downloadMusic(music:YouTube):
    '''
        this function download a video from youtube as mp4 (as audio)
        only the audio of the video is downloaded, then if you want to download
        the video you need to change the itag on line 54
    '''
    print(f"Downloading - {music.title}\nPlease wait...")
    music.streams.get_by_itag(140).download(f"musics/{music.author}")
    print("Download completed, enjoy!")

while True:
    print("========== Download from YouTube ==========")
    print("1 - Baixar música")
    print("2 - Baixar Playlist")
    print("0 - Sair")
    op = input("---> ")
    if op == '1':
        link = input("Informe o link\n--->")
        downloadMusic(YouTube(link))
    elif op == '2':
        link = input("Informe o link\n--->")
        downloadPlaylist(Playlist(link))
    elif op == '0':
        break
    else:
        print("Opção inválida :/")        
