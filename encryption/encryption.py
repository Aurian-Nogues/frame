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
            key_name: a string containing the name of the key (without extension)
        Return:
            the path to the key file
        Examples:
            x = Encryption()
            path = x.write_key('myKey')
        """
        key = Fernet.generate_key()
        key_folder = "key"
        key_file_name = str(key_name) + ".key"
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
            key = x.load_key('myKey')
            print(key)
            >> b'tnOND8Ey1Yz8WIoYrbBbauxwceaxByFMHwv_QW32iVs='
        """
        key_folder = "key"
        key_file_name = str(key_name) + ".key"
        key = open(os.path.abspath(os.path.join(key_folder,key_file_name)), "rb").read()
        self.key = key

        return key