# PiDoorOpener

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## How to use:
### Run the door. 
```
tmux
python reader.py
```
<kbd>CTRL</kbd>+<kbd>B</kbd> release then press <kbd>D</kbd> to detach the tmux session. 
Now you can just type: 
```
tmux attach
```
to load back up the python scipt. 

### Added Features. 
- sound effects (Need a speaker with aux cable connected to the Pi) 
- logs
- hashed keys

### Write keys. 
I decided to just create a authorized.txt file that contains the hashes of the IED numbers on the cards. 
To add a key into your list run the command:
```
python writer.py
```
It will ask you for username. (We are using the unviersities username.)

# Installation instructions. 
## Parts needed. 
- Raspberry Pi 2 (or newer)
- Servo (heavy torque)
- 1/16 cable (Or some sort of wire)
- RFID reader
    - We used this one from adafruit [PN532](https://www.adafruit.com/product/364) .
    - Works through doors. Great range.
###  Raspberry Pi
Install [raspbian lite](https://www.raspberrypi.org/downloads/raspbian/). 

###  RFID Reader
#### Installation

To install the library make sure your device is connected to the internet (with a wired or wireless connection), then
connect to the device's terminal and run the following commands (assuming a Debian-based operating system like
Raspbian, Debian, Ubuntu, etc.):

```
sudo apt-get update
sudo apt-get install build-essential python-dev git
git clone https://github.com/adafruit/Adafruit_Python_PN532.git
cd Adafruit_Python_PN532
sudo python setup.py install
```

Look inside the examples directory for a simple example of detecting and reading a MiFare classic card with readmifare.py.
Make sure to run examples as root using sudo, for example:
```
sudo python readmifare.py
```
Written by Tony DiCola for Adafruit Industries.
MIT license, all text above must be included in any redistribution

