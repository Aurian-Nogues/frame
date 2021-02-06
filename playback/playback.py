import vlc
import os
from time import sleep

#define paths
video_folder = os.path.abspath('videos')
video_name = 'test.mp4'
videos_path = os.path.abspath(os.path.join(video_folder, video_name))

print(videos_path)

# #create vlc media object
player = vlc.MediaPlayer(videos_path)
player.play()
sleep(4) #needs time to open vlc
while player.is_playing():
    sleep(1)
    