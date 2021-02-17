from administrator.encryption_admin.encryption import Encryption_admin

cypher = Encryption_admin()





if __name__ == "__main__":
    response=None
    menu_string = ("""
    0/ Repeat menu options
    1/ Write new code on card
    2/ Load a code from RFID card
    3/ Encrypt a video'
    Type \'exit\' to leave
    """)
    
    print(menu_string)
    while response != 'exit':

        response = input('Choose an option \n')

        if response == '0':
            print(menu_string)

        if response == '1':
            cypher.generate_new_key_rfid()

        if response == '2':
            cypher.load_encryption_key()

        if response == '3':
            cypher.encrypt_video()            
