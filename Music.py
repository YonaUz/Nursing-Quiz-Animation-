
"""
Created on Wed Jul 14 12:03:57 2021

@author: yonau
"""

#!/usr/bin/env python3
# Import playsound module
from playsound import playsound
 
# Input an existing mp3 filename
mp3File = str(input("Enter a mp3 filename: "))
# Play the mp3 file
playsound(mp3File)
playsound.stop()

