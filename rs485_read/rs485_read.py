#!/usr/bin/env python

#
# python sample application that reads from the raspicomm's RS-485 Port
#

import array
import serial

maxReadCount=10
readBuffer = array.array('c')

print('this sample application reads from the rs-485 port')

# open the port
print('opening device /dev/ttyRPC0')
try:
    ser = serial.Serial(port='/dev/ttyRPC0', baudrate=9600)
except:
    print('failed.')
    print('possible causes:')
    print('1) the raspicomm device driver is not loaded. type \'lsmod\' and verify that you \'raspicommrs485\' is loaded.')
    print('2) the raspicomm device driver is in use. Is another application using the device driver?')
    print('3) something went wrong when loading the device driver. type \'dmesg\' and check the kernel messages')
    exit()

print('successful.')

# read in a loop
print('start reading from the rs-485 port a maximum of ' + str(maxReadCount) + ' bytes')
readCount=0
while readCount < maxReadCount:
    readBuffer.append(ser.read(1))
    readCount=readCount+1

# print the received bytes
print('we received the following bytes:')
i=0
while i < maxReadCount:
    val=ord(readBuffer[i])
    hx=''
    if val >= 32 and val <= 126:
        hx=' - \'{0}\''.format(readBuffer[i])
    print('[{0:d}]: 0x{1:x}{2}'.format(i, val, hx))    
    i=i+1
