from cryptography.fernet import Fernet
import os
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522



class UserCipher:
    def __init__(self):
        self.key = None

    def load_key(self):
        """
        Loads en encryption key from an RFID card
        Note that key is loaded at string and converted as byte
        """
        reader = SimpleMFRC522()
        print("scan a card")
        try:
            id, text_key = reader.read()
            text_key = text_key.rstrip() #remove white space at end of string
            key = text_key.encode()
            self.key = key
        finally:
            GPIO.cleanup()
            print('Key successfully loaded')

    def decrypt_video(self):
        """
        Decrypts a file into the ramdisk
        This requires a key to be loaded from RFID card
        The file to be decrypted is from user/videos
        If only one file is present it will directly decrypt
        Otherwise it will prompt user to choose which file to decrypt
        """
        if self.key is None:
            self.load_key()
        
        input_folder = os.path.abspath(os.path.join('user', 'videos'))
        output_folder = os.path.abspath('/mnt/ramdisk')
        files_in_folder = os.listdir(input_folder)
        #remove __init__
        files_in_folder.remove('__init__.py')
        if len(files_in_folder) > 1:
            print('Which file do you want to play ?')
            i=1
            for file in files_in_folder:
                print(str(i) + '/ ' + str(file))
                i+=1
            
            # get user input to choose which file to encrypt
            validation = False
            # validate inputs
            while validation is not True:
                response = input('Select a number\n')
                failed=False
                try:
                    response = int(response)
                    if response > len(files_in_folder):
                        print('This number is bigger than the number of files')
                        failed=True
                except ValueError:
                    print('You should input a number')
                    failed=True
                    
                if failed is False:
                    validation = True
                    file_to_decrypt = files_in_folder[response - 1]
        else:
            file_to_decrypt = files_in_folder[0]
        
        decrypted_file_name = str(file_to_decrypt).replace('.encrypted', '.mp4')
        encrypted_location = os.path.abspath(os.path.join(input_folder, file_to_decrypt))
        decrypted_location = os.path.abspath(os.path.join(output_folder, decrypted_file_name))

        f=Fernet(self.key)
        #read bytes of encryted file
        encrypted = open(encrypted_location, 'rb')
        encrypted_bytes = encrypted.read()
        #decrypt bytes
        decrypted_bytes = f.decrypt(encrypted_bytes)
        #store decrypted bytes in ramdisk
        decrypted_file = open(decrypted_location, 'wb')
        decrypted_file.write(decrypted_bytes)
        
        
    @staticmethod
    def delete_on_interrupt():
        """
        This will remove any file in ramdisk
        Use it on interrupt command to cleanup volatile memory
        """

        ramdisk_location=os.path.abspath('/mnt/ramdisk')
        files_to_delete = os.listdir(ramdisk_location)
        for file in files_to_delete:
            os.remove(os.path.join(ramdisk_location, file))


if __name__ == "__main__":
    cipher = UserCipher()
    cipher.delete_on_interrupt()
    