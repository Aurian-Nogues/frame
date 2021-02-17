import vlc
import os
from time import sleep
import subprocess


class VideoPlayer:
    def __init__(self, video_name):
        ramdisk_location=os.path.abspath('/mnt/ramdisk')
        self.video_path = os.path.abspath(os.path.join(ramdisk_location, video_name))
        #omxplayer --loop <file>

    def play(self):
        subprocess.Popen(['vlc', self.video_path, '--loop', '--fullscreen'])

    # def old_code(self):

    #     #define paths
    #     video_folder = os.path.abspath('videos')
    #     video_name = 'test.mp4'
    #     videos_path = os.path.abspath(os.path.join(video_folder, video_name))
    #     # # #create vlc media object
    #     # player = vlc.MediaPlayer(videos_path)
    #     # player.set_fullscreen(True)
    #     # player.play()
    #     # sleep(4) #needs time to open vlc
    #     # while player.is_playing():
    #     #     sleep(1)
    
if __name__ == "__main__":
    player = VideoPlayer('test.mp4')
    player.play()
