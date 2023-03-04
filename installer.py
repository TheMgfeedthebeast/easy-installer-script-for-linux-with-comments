
#this is a free installer app for linux made with python made by mgfeedthebeast 
#do not delete theese lines you can use this program for what you want so long its not maliscius
#this code is not copyrighted but credit me if you use it 
#thanks for using my code (:

#everything is commented so you can easly modify it:

import time #importing time lib
from time import sleep #importing sleep from the time lib
import subprocess #importing subprocess for the ability to run terminal commands

print("loading...") #prints to the user that the script is working and is going to load

sleep(5) #sleeps for five seconds

print("launching scripts...") #prints to the user that the script is working and is going to load

pyver = ("1","2") #creates the two options
aa = None #creates a var for what the user chose to do

while aa not in pyver: #make sure that the user gives a actual correct input
    aa = input("do you want to install 1(py3) or 2(py2): ") #askes the user for what to install
    if aa == "1": #checks if the user selected option one 
        print("you selected py3...") #says what the user selected
        sleep(3) #sleeps for three seconds
        print("installing...") #prints to the user that the program installs the package
        package_name = "python3" #configures what package to install
        subprocess.run(["sudo", "apt-get", "install", package_name]) #installs the package using subprocess
                
    elif aa == "2": #checks if the user selected option two 
        print("you selected py2...") #says what the user selected
        sleep(3) #sleeps for three seconds 
        print("installing...") #prints to the user that the program installs the package
        package_name = "python2" #configures what package to install
        subprocess.run(["sudo", "apt-get", "install", package_name]) #installs the package using subprocess
        
print("done!") #tells the user that its done
sleep(5) #sleeps for five seconds
print("cleaining up!") #tells that its cleaning up, which is not done with this script but something you can add
sleep(3) #sleeps for three seconds
print("done!") #tells the user that its done
sleep(3) #sleeps for three seconds
