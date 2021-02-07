from playback.playback import VideoPlayer
from encryption.encryption import Encryption

if __name__ == "__main__":
      #decrypt video
      cypher = Encryption()
      cypher.load_key('myKey.key')
      cypher.decrypt_file('test.encrypted', 'test.mp4')

      #read video
      player = VideoPlayer('test.mp4')
      player.play()
