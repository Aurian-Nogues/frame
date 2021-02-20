import os
import subprocess

class VideoPlayer:
    def __init__(self):
        ramdisk_location=os.path.abspath('/mnt/ramdisk')
        files_in_folder = os.listdir(ramdisk_location)
        if len(files_in_folder) > 1:
            raise Exception('There should not be more than 1 file in ramdisk, something went wrong')
        elif len(files_in_folder) == 0:
            raise Exception('No files to play in folder')
        self.video_path = os.path.abspath(os.path.join(ramdisk_location, files_in_folder[0]))
        self.script_path = "./user/video_player/play.sh"


    def play(self):
        subprocess.check_call([self.script_path, self.video_path])

if __name__ == "__main__":
    player = VideoPlayer()
    player.play()