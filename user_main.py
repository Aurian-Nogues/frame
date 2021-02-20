from user.encryption_user.encryption import UserCipher

if __name__ == "__main__":
    cipher = UserCipher()

    try:
        cipher.decrypt_video()
    except:
        cipher.delete_on_interrupt()