import socket
import sys
import subprocess
import os
from ping3 import ping
import psutil
from termcolor import colored
import time

# CMD windows options
os.system('mode 45, 15')
os.system('color')

# for Windows10 some text output will be colorised.
winver = str(sys.getwindowsversion())
winver10 = 'major=10'

# Change here to your subnet
subnet = '192.168.1.'

def start():  # Starting point
    global winver, winver10
    os.system('cls') # Function "start()" will be calling very often so its need to clear all text under to start again. Beautiful!
    choice = False
    while not choice:
        try:
            if winver10 in winver:
                ip = int(input("IP-address: "+colored(subnet, 'red')))
            else:
                ip = int(input("IP-address: "+subnet))
            if ip >= 1 and ip <= 255:
                full_ip = subnet+str(ip) # Host's IP-address. Thats what we needed from user's input.
                checking(full_ip)
            else:
                choice = False
        except ValueError:
            choice = False

def checking(ipaddr):
    global winver, winver10
    os.system('cls')
    # First string in output will be host response (by ICMP ping).
    print(colored('IP-address: ','green')+ipaddr)
    print('Status:')
    response = ping(ipaddr)
    if response == None: # If user is not responding => exit to starting point
        if winver10 in winver:
            os.system('cls')
            print(colored('IP-address: ','green')+ipaddr)
            print('Status: ' + colored('OFFLINE', 'red'))
            time.sleep(3)
            exiting_count()
        else:
            os.system('cls')
            print('IP-address: ' + ipaddr)
            print(ipaddr+' - ' + 'OFFLINE')
            time.sleep(2)
            exiting_count()
    else: #Okay. Host is online. Lets type it to user
        os.system('cls')
        if winver10 in winver:
            print(colored('IP-address: ','green')+ipaddr)
            print('Status:' + colored(' ONLINE', 'green'))
        else:
            print("Status: ONLINE")
        LM_checkin(ipaddr) # Going to check his opened sockets for remote admin soft

def LM_checkin(ipaddr):
    LM_port = [5650] # Classic LiteManager socket
    for port in LM_port:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ipaddr,port))
        except socket.error: #So if LM socket closed - we will gonna check RAdmin socket next.
            if winver10 in winver:
                print('LiteManager' + colored(' is closed', 'red'))
            else:
                print('LiteManager is closed')
            RA_checkin(ipaddr)
        else:
            s.close
            if winver10 in winver:
                print ('LiteManager'+colored(' is open','green')+'. Connnecting..')
            else:
                print ('LiteManager is open. Connecting..')
            try:
                subprocess.Popen(["C:\Program Files (x86)\LiteManager Pro - Viewer\ROMViewer.exe", "/name:"+ipaddr, "/fullcontrol"])
                time.sleep(1)
                exiting_count()
            except FileNotFoundError: #Execption if LiteManager isn't installed on default path
                if winver10 in winver:
                    print(colored('Error. LiteManager Viewer is not installed on default path. Please install it and repeat.', 'red'))
                else:
                    print('Error. LiteManager Viewer is not installed on default path. Please install it and repeat.')
                time.sleep(1)
                exiting_count()

def RA_checkin(ipaddr):
    radmin_port = [4899] # Classic RAdmin socket
    for port in radmin_port:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ipaddr,port)) # Checkin socket opening
        except socket.error: # Its closed
            if winver10 in winver:
                print('Radmin'+colored(' is closed','red'))
            else:
                print('Radmin is closed')
            time.sleep(2)
            exiting_count()
        else: # Its opened
            s.close
            if winver10 in winver:
                print('RAdmin'+colored(' is open. ','green')+'Connecting..')
            else:
                print('RAdmin is open. Connecting..')
            try:
                subprocess.Popen(["C:\Program Files (x86)\Radmin Viewer 3\Radmin.exe", "/connect:"+ipaddr])
                time.sleep(1)
                exiting_count()
            except FileNotFoundError: # Execption if RAdmin isn't installed on default path
                if winver10 in winver:
                    print(colored('Error. Radmin Viewer is not installed on default path. Please install it and repeat.', 'red'))
                else:
                    print('Error. Radmin Viewer is not installed on default path. Please install it and repeat.')
                time.sleep(1)
                exiting_count()

def exiting_count():
    global winver, winver10
    for i in range (3,0,-1):
        os.system('cls')
        if winver10 in winver:
            print(colored('Exiting to the main menu in ','white')+colored('%d' %i,'red')+' sec')
        else:
            print('Exiting to the main menu in %d' %i+' sec')
        time.sleep(0.5)
    start()

start()