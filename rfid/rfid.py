import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def write_data():

    try:
        text = input("New data:")
        print("now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()

def read_data():
    print("Scan a card\\")
    try:
        id, text = reader.read()
        return id, text
        

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    read_data()