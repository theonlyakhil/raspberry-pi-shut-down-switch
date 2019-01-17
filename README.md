# Raspberry Pi Power button Switch 
The repository contains the code to use a button as a shutdown switch for Raspberry Pi.

# Requirements

1. Raspberry Pi
2. button
3. wire - 2

# Instructions

1. Connect one side of the switch to GPIO 4 and the other side of the switch to 3.3v.
2. Now, we have to run the python code at boot. We will make a folder to save the python code.
```
$ cd /home/pi
$ mkdir service
$ cd service
```
3. Move the code to this folder.
4. Now, we have to create a unit file for systemd
```
$ sudo nano /lib/systemd/system/powerbutton.service
```
5. Add the following code to the file.
```
[Unit]
 Description=Power button controller
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python /home/pi/service/button.py

 [Install]
 WantedBy=multi-user.target
```
6. Set permission for the unit file to 644.
```
$ chmod 644 /lib/systemd/system/powerbutton.service
```
7. Now, we tell systemd to start the python code at boot.
```
$ sudo systemctl daemon-reload
$ sudo systemctl enable powerbutton.service
```

# Contributors

1. [Akhil A](https://github.com/theonlyakhil)
2. [Sashwat K](https://github.com/sashuu6)
