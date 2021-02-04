from encryption.encryption import Encryption


if __name__ == "__main__":
      x = Encryption()
      x.write_key('myNewKey')
      key = x.load_key('myNewKey')
      print(key)
      print(x.key)