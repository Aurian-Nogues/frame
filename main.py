from playback.playback import VideoPlayer
from encryption.encryption import Encryption
from time import sleep

if __name__ == "__main__":

      try:
            #decrypt video
            cypher = Encryption()
            cypher.load_key('myKey.key')
            cypher.decrypt_file('test.encrypted', 'test.mp4')

            #read video
            player = VideoPlayer('test.mp4')
            player.play()

            #need to keep that so the program never finishes which means any exception / keyboard interrupt will trigger the except
            while True:
                  sleep(1)
                  
      except:
            Encryption.delete_on_interrupt()



