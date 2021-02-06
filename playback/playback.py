import vlc
import os

#define paths
video_folder = os.path.abspath(os.path.join('..', 'videos'))
video_name = 'non_encrrypted.mkv'
videos_path = os.path.abspath(os.path.join(video_folder, video_name))

# #create vlc media object
player = vlc.MediaPlayer('1.mp4')
player.play()