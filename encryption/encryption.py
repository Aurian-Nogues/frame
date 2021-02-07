from cryptography.fernet import Fernet
import os

class Encryption:
    def __init__(self, key_folder = os.path.abspath(os.path.join('..', 'key'))):

        self.key_folder = key_folder
        self.key = None

    def write_key(self, key_name):
        """
        Generates a key file and store it into they key folder
        Params:
            key_name: a string containing the name of the key (with extension)
        Return:
            the path to the key file
        Examples:
            x = Encryption()
            path = x.write_key('myKey.key')
        """
        key = Fernet.generate_key()
        key_folder = "key"
        key_file_name = str(key_name)
        with open(os.path.abspath(os.path.join(key_folder,key_file_name)), "wb") as key_file:
            key_file.write(key)
        return os.path.abspath(os.path.join(key_folder,key_file_name))


    def load_key(self, key_name):
        """
        Loads the key from the current directory named `key`
        also loads the key in a self.key attribute
        Params:
            key_name: a string containing the name of the key to retrieve from the key/ folder
        Return: the key

        Examples
            x=Encryption()
            key = x.load_key('myKey.key')
            print(key)
            >> b'tnOND8Ey1Yz8WIoYrbBbauxwceaxByFMHwv_QW32iVs='
        """
        key_folder = "key"
        key = open(os.path.abspath(os.path.join(key_folder,key_name)), "rb").read()
        self.key = key

        return key

    def encrypt_file(self,input_file, output_file, input_folder = 'videos', output_folder = 'videos'):
        if self.key is None:
            raise Exception("You need to first load a key is Encryption.load_key(key_name)")

        input_video_location = os.path.abspath(os.path.join(input_folder, input_file))
        output_video_location = os.path.abspath(os.path.join(output_folder, output_file))
        
        non_encrypted = open(input_video_location, 'rb')
        temp = non_encrypted.read()

        f = Fernet(self.key)
        encrypted = f.encrypt(temp)

        encrypted_file= open(output_video_location, 'wb')
        encrypted_file.write(encrypted)

    def decrypt_file(self,input_file_name, output_file_name, input_folder = 'videos'):
        """
        Decrypts a file into the ramdisk
        This requires a key to already be loaded

        Params:
            input_file_name: str name of encrypted file to decrypt (eg: 'myVideo.encrypted')
            output_file_name: str the name of the file after decription (eg: 'myVideo.mp4')
            input_folder: folder where the video to decrypt is located, defaults to 'videos' folder

        Examples:
              cypher = Encryption()
              cypher.load_key('myKey.key')
              cypher.decrypt_file('test.encrypted', 'test.mp4')

              >> file is now available as test.mp4 in the mnt/ramdisk location
              >> this is volatile memory folder so this file will be lost if computer is shutdown
        """

        if self.key is None:
            raise Exception("You need to first load a key is Encryption.load_key(key_name)")
        
        ramdisk_location=os.path.abspath('/mnt/ramdisk')
        input_video_location = os.path.abspath(os.path.join(input_folder, input_file_name))
        output_video_location = os.path.abspath(os.path.join(ramdisk_location, output_file_name))

        f = Fernet(self.key) #generate fernet cypher

        #read bytes of encryted file
        encrypted = open(input_video_location, 'rb')
        encrypted_bytes = encrypted.read()
        #decrypt bytes
        decrypted_bytes = f.decrypt(encrypted_bytes)
        #store decrypted bytes in ramdisk
        decrypted_file = open(output_video_location, 'wb')
        decrypted_file.write(decrypted_bytes)

if __name__ == "__main__":
    x=Encryption()
    x.load_key('myKey')

    
