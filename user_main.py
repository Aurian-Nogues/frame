from user.encryption_user.encryption import UserCipher
from user.video_player.player import VideoPlayer
from time import sleep

if __name__ == "__main__":
    while True:
        cipher = UserCipher()

        try:
            cipher.decrypt_video()
            player = VideoPlayer()
            player.play()
            #need to keep that so the program never finishes which means any exception / keyboard interrupt will trigger the except
            while True:
                sleep(1)

        except:
            cipher.delete_on_interrupt()
        finally:
            cipher.delete_on_interrupt()