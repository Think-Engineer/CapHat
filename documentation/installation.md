# CapHat Getting Started Guide

In order to get up and running with the CapHat when it comes through your door we've provided a handy get up and running guide below. 

# Table of Contents
1. [Setting up your Raspberry Pi](#Setting)
3.1. [Initialising up I2C](#Initialising)
2. [Cloning This Repo](#Cloning)
3. [Installing the Adafruit MPR121 Library](#Installing)
4. [Running your first demo](#Running)

## Setting Up Your Raspberry Pi
If you have received a full kit from us, or have purchased a Raspberry Pi to use with your caphat the first thing you are going to need to do is setup your Raspberry Pi with the Raspbian Operating System (OS). There is much better advice [here](https://www.howtoforge.com/tutorial/howto-install-raspbian-on-raspberry-pi/) than we will ever be able to summarise so go and follow that tutorial and then pop back to setup your CapHat.

### Initialising up I2C
I2C is a communication method that is used to communicate with the CapHat. We use I2C so you can connect multiple devices without worrying about using up lots of GPIO pins so you can continue using them for your projects.

The Raspberry Pi needs to be told that it is allowed to commuincate using I2C and Adafruit provide a great tutorial on how to setup I2C. Click [Here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) and follow down to the end of Installing Kernel Support (with Raspi-Config), don't forget the commands before that section.

You will need to update the /boot/config.txt file.  Open the file with nano using the command:

`sudo nano /boot/config.txt`

Add the following text to the bottom of the file:

`dtparam=i2c1=on`
`dtparam=i2c_arm=on`

Save your changes and exit the nano editor.
All versions:
Set the Raspberry Pi to start I2C automatically at boot by editing /etc/modules :

`sudo nano /etc/modules`

Use your cursor keys to move to the last line and add a new line and then add:

`i2c-dev`

Save your changes and exit the nano editor.

To avoid having to run the I2C tools at root add the ‘pi’ user to the I2C group:
`sudo adduser pi i2c`

Next reboot the Raspberry Pi:
`sudo reboot`

When your Raspberry Pi has rebooted you will now have I2C and SMBus Python 2 or 3 support.


## Cloning This Repo
If you haven't done already, you are going to need to clone this repo onto your Raspberry Pi to access all the goodies stored within.

Navigate to the folder on your Raspberry Pi you want to download to and run the following command:
`git clone https://github.com/Think-Engineer/CapHat.git`

## Installing the Adafruit MPR121 Library
In the Software folder we have provided the Adafruit MPR121 library. This Library is fantastic and creates a great set of functions for us to talk to and use the capactive touch sensing chip that is located on the boards.

We need to run the setup file inside of this library in order to get the python library all setup. Navgiate to this folder inside a terminal and run the following commands:

`sudo apt-get install build-essential python-dev python-smbus python-pip git`
`sudo python setup.py install`

The setup script will download a few dependencies and install the library.  If there are errors, carefully check all the dependencies above were installed and try again.

That's it, the MPR121 library is now installed!  Continue on to learn how to run an example program and learn how to use the library.

## Running your first demo
Once you have completed all the previous sections you will now be ready to run your first CapHat Demo!

Plug the CapHat in to the Raspberry Pi as shown in the following image
![alt text](https://github.com/Think-Engineer/CapHat/documentation/ConnectionGuide.png "CapHat Connection")

Run the following commands to navigate to the Demos Folder

`cd Software/Demos`

And you should be able to run the full_keypad demo which will put every button press (and release) on the screen!

`sudo python full_keypad.py`




