**Preparation Sequence for a Radxa ROCK 5C Card to Work with the "Ensor-384" Audio Recorder Card**

1\. Required Items

\- Radxa ROCK 5C Card

\- Original Radxa Power Supply with USB-C Cable

\- rock-5c\_bookworm\_cli\_b1.output.img.xz Operating System

\- RJ45 Ethernet Cable

\- HDMI to HDMI Cable

\- Wireless Keyboard with Mouse

\- Original 8GB Micro SD Card

\- Computer with Ubuntu 22.04.4 operating system and internet connection

\- Ensor-384 Sound Recorder Card

\- The ensor384\_rock\_5C.zip file downloaded from the internet

\- 64GB or larger USB flash drive, formatted in exFAT for recordings

\- The ensor384\_rock\_5C.zip file will be extracted to the USB flash drive

2\. Install the operating system "rock-5c\_bookworm\_cli\_b1.output.img.xz" without a desktop environment.

Use the balenaEtcher application from Linux to write the image.

The default username and password for the written image are:

username: rock  
password: rock

After writing the card, you can view and edit two configuration files:

before.txt

config.txt

3\. Edit the before.txt file, Radxa First Boot Configuration, to enable the SSH service, which is disabled by default.

Simply comment out the following lines:

	disable\_service ssh  
	disable\_service smbd  
	disable\_service nmbd

It should look like this:

	\# Disable services

	\# Command:

	\# disable\_service \<systemd unit name\>

	\#  
	\#disable\_service ssh

	disable\_service smbd

	disable\_service nmbd

Insert the microSD card into the radxa ROCK 5C and check that it is properly inserted

Connect the HDMI cable if you have a monitor

Connect the USB-C to USB-C power cable

And finally

Connect the power supply to the electrical outlet

4\. Find the IP address of the radxa ROCK 5C

Boot the system with a keyboard and monitor

To find the assigned IP address, enter the command

ip a

Also, with Ubuntu, you can scan the network with the nmap application

install nmap on your computer with ubuntu 

sudo apt update   
sudo apt install nmap 

To scan a local network (for example, 192.168.1.0/24), you can use the following command: 

nmap \-sn 192.168.0.0/24 

Starting Nmap 7.80 (https://nmap.org) at 2024-08-23 19:14 CEST   
Nmap scan report for 192.168.0.1   
Host is up (0.0025s latency).   
Nmap scan report for rock-5C (192.168.0.52)   
Host is up (0.0039s latency).   
Nmap done: 256 IP addresses (2 hosts up) scanned in 4.34 seconds

This IP address will be used for the SSH connection using PuTTY.

5\. Install PuTTY on the computer running Ubuntu 22.04.4 to send commands via SSH to the RADXA ROCK-5C network interface.

sudo apt install putty

Verify that PuTTY is working.

All the following commands will be executed via SSH using PuTTY.

6\. Important\!\!\! DO NOT update the rock-5C operating system

because it will cause TDM to stop working

The operating system that works correctly is the following Debian image:

ROCK 5C Lite CLI System Image: Debian 12 CLI b1

rock-5c\_bookworm\_cli\_b1.output.img.xz

7\. Check the label of the exFAT formatted USB flash drive

	sudo fdisk \-l

		\> /dev/sda1

The USB flash drive will be used to store the audio recordings

1 hour of audio recording, 2 stereo channels at 192000 m/s and 32-bit resolution, takes up 5.4 GB

1 hour of audio recording, 2 stereo channels at 384000 m/s and 32-bit resolution, takes up 10.8 GB

8\. Mount the USB drive at system startup

The USB flash drive will be mounted in the following path:

/media/rock/Ensor384

Create \`rock/Ensor384\` directories in \`/media

	sudo mkdir \-p /media/rock/Ensor384

Full permissions enabled for everyone

	sudo chmod \-R 777 /media/rock/Ensor384

Edit and add the line to the \`/etc/fstab\` file

	sudo nano /etc/fstab

/dev/sda1 /media/rock/Ensor384 auto auto,user,rw,umask=000,nofail,x-system.device-timeout=10	0	0

Verify that the modifications to \`/etc/fstab\` are correct

	sudo mount \-a  
	sudo systemctl daemon-reload

	sudo reboot

to verify that the USB drive mounts correctly

9\. Copy the Ensor folder from the USB drive to /home/rock/

The USB drive will contain the recording configuration file:

ensor.conf

and the "Ensor" directory, which should be copied to:

/home/rock/

	cp \-dr /media/rock/Ensor384/Ensor /home/rock/

Once the Ensor directory is copied, you can delete it from the USB drive if desired.

	rm \-dr /media/rock/Ensor384/Ensor

10\. Compile MRAA to manage the GPIO pins of the 40-pin connector

Run all the following commands via SSH using PuTTY

To facilitate command entry, these will be copied from this file and pasted into the PuTTY console (use the middle mouse button to paste the command).

Install MRAA

Uninstall the system stock package:

	cd /

	sudo apt purge \*mraa\* 

Source code installation 

	sudo apt-get update \-y   
	sudo apt-get install git cmake build-essential swig python3-dev libnode-dev cmake libjson-c-dev libgtest-	dev pkg-config cmake-data \-y 

	sudo git clone https://github.com/nascs/mraa.git   
	mraa cd   
	sudo git checkout \-b Add\_Radxa\_ROCK5C\_Support origin/Add\_Radxa\_ROCK5C\_Support   
	sudo mkdir build && cd build   
	sudo cmake .. && sudo make ${nproc} && sudo make install && sudo ldconfig

MRAA Command Line Tools  
GPIO 

	mraa-gpio list: List all available pins   
	mraa-gpio get pin: Get Pin Status   
	mraa-gpio set pin level: Set Pin Status   
	mraa-gpio version: Get MRAA Version

11\. Run \`sudo rsetup\`

Enable the following DTS:

\*Enable I2C8-M2

	rsetup  
		overlays  
			Manage overlays

				\*Enable I2C8-M2

Load the DTS file from the "Ensor-384" audio recording card using \`rsetup\`

	rsetup  
		overlays  
			Install 3rd party overlay

				/home/rock/Ensor/dts/tdm.dts

	sudo reboot

12\. Reboot the system and verify that the ENSOR-384 recording card has been installed

		arecord \-l

		Test that card is 2 y device is 0

		  
13.- Verify that the card records audio at a sampling rate of 192000 samples/s and 32 bits

 The recording program is located in /home/rock/Ensor/tdm.py

and the recording configuration file, ensor.conf, is located in /media/rock/Ensor384/ensor.conf

Open the file /media/rock/Ensor384/ensor.conf using nano and run the desired recording program, either tdm.py or eea.py

You need to use "sudo" to change the system date.

For 4-channel TDM recording:

	sudo /home/rock/Ensor/tdm.py

For 2-channel I2S (stereo) recording:

	sudo /home/rock/Ensor/eea.py

Try recording with the default settings of 192000 m/s and 32 bits.  
The recording will be a 10-second file.

13\. Recording at System Boot

We will use the init.service.

We will create the file /etc/systemd/system/init.service

	sudo nano /etc/systemd/system/init.service

		\[Unit\]

		Description=recorder service

		\#After=network.target network-online.target

		\#Wants=network-online.target

		\[Service\]

		ExecStart=/home/rock/Ensor/recorder.sh

		\[Install\]  
		WantedBy=multi-user.target  
Enable init.service to start when the system boots

	sudo systemctl enable /etc/systemd/system/init.service

14\. Scripting /home/ensor/Ensor/recorder.sh

	nano /home/rock/Ensor/recorder.sh

		\#\!/bin/sh

		\#sudo /home/ensor/Ensor/tdm.py

		\#sudo /home/ensor/Ensor/eea.py

		\#sudo shutdown \-h now

Only enable the program you need.

If you want the system to shut down when recording is complete, enable the following line:

	sudo shutdown \-h now

This script starts recording according to the ensor.conf configuration and, when finished, shuts down the system to save power.

15.- make a backup of the card image on the USB flash memory using “dd” command

from rock-5c: 

Check uSD card 

	sudo fdisk \-l 

		Disk /dev/mmcblk1: 7.4 GiB, 7948206080 bytes, 15523840 sectors   
		Units: sectors of 1 \* 512 \= 512 bytes   
		Sector size (logical/physical): 512 bytes / 512 bytes   
		I/O size (minimum/optimal): 512 bytes / 512 bytes   
		Disklabel type: gpt   
		Disk identifier: 3B224E8F-6BA8-4923-AB39-B84CF5D0E668 

sudo dd if=/dev/mmcblk1 of=/media/rock/Ensor384/Ensor384\_rock5C.img bs=4M status=progress