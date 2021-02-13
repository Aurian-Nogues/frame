from playback.playback import VideoPlayer
from encryption.encryption import Encryption
from time import sleep
from rfid.tests import read_data

if __name__ == "__main__":

      id, text = read_data()
      

      try:
            #decrypt video
            cypher = Encryption()
            cypher.load_key('myKey.key')
            cypher.decrypt_file('test_girl.encrypted', 'test.mp4')

            #read video
            player = VideoPlayer('test.mp4')
            player.play()

            #need to keep that so the program never finishes which means any exception / keyboard interrupt will trigger the except
            while True:
                  sleep(1)
                  
      except:
            Encryption.delete_on_interrupt()



