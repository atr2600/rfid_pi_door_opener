
import os
import binascii
import sys
import time
import Adafruit_PN532 as PN532
import lars
import hashlib
import uuid

# Setup how the PN532 is connected to the Raspbery Pi/BeagleBone Black.
# It is recommended to use a software SPI connection with 4 digital GPIO pins.

# Configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Configuration for a BeagleBone Black:
# CS   = 'P8_7'
# MOSI = 'P8_8'
# MISO = 'P8_9'
# SCLK = 'P8_10'

# Create an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

#OPENING FILE
#f = open("authorized.txt", "r")
log = open("door.log", "a")

def hash_key(key):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(key.encode()).hexdigest()

def check_key(user_key):
    with open("authorized.txt","r") as f:
        for line in f.readlines():
            hashed_key, salt, username = line.split(":")
            return hashed_key == hashlib.sha256(salt.encode() + user_key.encode()).hexdigest()


# Main loop to detect cards and read a block.
print('Waiting for MiFare card...')
while True:
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        continue
    if check_key('{0}'.format(binascii.hexlify(uid))):
        check = True
    if check:
        os.system('mpg123 audio.mp3 &')
	lars.opendoor()
        log.write("Open door at " + time.strftime("%c") + "\n") #need to add user data on this one. 
    else:
        log.write("WARNING!!! Attempt to open door at " + time.strftime("%c") + " with key tag: " + '{0}'.format(binascii.hexlify(uid)) + "\n")
    time.sleep(2)
    # print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
    # print('{0}'.format(binascii.hexlify(uid)))
    # username = raw_input("Type in the username of this ID tag: ")
    # f.write('{0}'.format(binascii.hexlify(uid)) + "," + username + "\n")
    # quit()
