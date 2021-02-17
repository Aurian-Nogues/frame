from cryptography.fernet import Fernet
import os
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Encryption_admin:
    def __init__(self):
        self.key = None

    def generate_new_key_rfid(self):
        """
        This will generate a secret key and write it onto an RFID card
        Note that key is generated as bytes and stored as string
        """

        key = Fernet.generate_key()
        str_key = key.decode()

        reader = SimpleMFRC522()
        try:
            print('Place the card on reader')
            reader.write(str_key)
            return key
        finally:
            print("key successfully loaded on card")
            GPIO.cleanup()

    def load_encryption_key(self):
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

    def encrypt_video(self):

        # get code from card if not already loaded
        if self.key is None:
            print('No key is currently loaded')
            self.load_encryption_key()

            #scan folder to show available files
            input_folder = os.path.abspath(os.path.join('administrator', 'videos', 'non_encrypted'))
            files_in_folder = os.listdir(input_folder)
            #remove __init__
            files_in_folder.remove('__init__.py')
            print('Which file do you want to encrypt ?')
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
                    if (response - 1) > len(files_in_folder):
                        print('This number is bigger than the number of files')
                        failed=True
                except ValueError:
                   print('You should input a number')
                   failed=True
                   
                if failed is False:
                    validation = True
            
            # encrypt file in folder
            file_to_encrypt = files_in_folder[response - 1]
            output_folder = os.path.abspath(os.path.join('administrator', 'videos', 'encrypted'))
            encrypted_file_name = str(file_to_encrypt).replace('.mp4', '.encrypted')

            non_encrypted = open(os.path.abspath(os.path.join(input_folder, file_to_encrypt)), 'rb')
            temp = non_encrypted.read()
            f = Fernet(self.key)
            encrypted = f.encrypt(temp)

            encrypted_file= open(os.path.abspath(os.path.join(output_folder, encrypted_file_name)), 'wb')
            encrypted_file.write(encrypted)

            print('File successfully encrypted at ' + str(os.path.abspath(os.path.join(output_folder, encrypted_file_name))))


if __name__ == "__main__":
    enc = Encryption_admin()
    enc.encrypt_video()

