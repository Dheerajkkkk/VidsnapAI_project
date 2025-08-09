# this file lookinto the folder that user has uploaded and covert them into videos
import os
from text_to_audio import text_to_speech_file
import time
import subprocess

def text_to_audio(folder):
    print("TA - ", folder)
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)

def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4
'''
    subprocess.run(command, shell=True, check=True)
    print("CR - ", folder)

if __name__ == "__main__":
    while True:
        print("proccessing queue")
        with open("done.txt", "r") as f:
            done_folder = f.readlines()

        done_folder = [f.strip() for f in done_folder]
        folders = os.listdir("user_uploads")
        print(folders, done_folder)
        for folder in folders:
            if(folder not in done_folder):
                text_to_audio(folder)  # to covert the text into mp3 audio
                create_reel(folder) # to covert the images and ausio to reels
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)




