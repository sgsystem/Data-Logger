# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:11:20 2018

@author: Tsvetomir Gotsov
Data Logger V0.0.1 - First Realese 5.3.2018

"""
import os
import time
from datetime import datetime
from time import sleep

date = time.strftime("%d.%m.%Y.")
file_name = str(date) + "_log10.csv"
first_line = "sep=,"
PATH = "G:\\"
 
#For every day new file!
try:
    file = open(str(PATH) + str(file_name), 'a+') #Opens a file for both appending and reading
    if os.path.isfile(str(PATH) + str(file_name)):
        print("File does exist at G")    
except:
    file = open(file_name, 'a+')
    if os.path.isfile(file_name):
        print("File does exist at current directory")
    else:
        print("No such file exists at this time")
#print (os.path.abspath(file_name)) #Print path from file
file.seek(0) #Go to first line in file
first = file.read(5)
#Set the first line in file
if first != first_line:
    print("New file, write first line")
    file.write(first_line)            #Set seperator for Exsel, This text in a first line in every new file!
    file.write("\n Time, Sensor1, Sensor2, Sensor3, Sensor4, Sensor5\n")
i = 0
file.seek(2) #Go to end of file
while True:
        i = i + 1
        #now = datetime.now()
        #now = time.strftime("%d.%m.%Y.%H.%M.%S")
        now = time.strftime("%H.%M.%S")
        file.write(str(now)+","+str(i)+","+str(i)+","+str(i)+","+str(i)+","+str(i)+"\n")
        file.flush()
        time.sleep(2)
file.close()