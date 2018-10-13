#	 ______________            ______ _____       ______________ ______
# ___  __ )__  /_____ _________  /____(_)________  __ \_  __ \/__  /
# __  __  |_  /_  __ `/  ___/_  //_/_  /__  ___/  / / /  / / /__  / 
# _  /_/ /_  / / /_/ // /__ _  ,<  _  / _(__  )/ /_/ // /_/ / _  /  
# /_____/ /_/  \__,_/ \___/ /_/|_| /_/  /____/ \____/ \____/  /_/   

# Author: Sashwat K
# Created On: 13 Oct 2018
# Revision: 1
# Last Edited: 13 Oct 2018

import RPi.GPIO as GPIO
import subprocess

while True:
	if GPIO.input(4):
        #print("Performing Shitdown...")
        cmd = "sudo halt"
        subprocess.check_output(cmd, shell = True )