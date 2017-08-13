#!/usr/bin/env python

import sys
import os

"""
def start_cam():
    while True:
        #Initializes an instance of Zbar to the commandline to detect barcode data-strings.
        p=os.popen('/usr/bin/zbarcam --prescale=320x240','r')
        #Barcode variable read by Python from the commandline.
        print("Please Scan a QRcode to begin...")
        barcode = p.readline()
        barcodedata = str(barcode)[8:]

        if barcodedata:
            print("{0}".format(barcodedata))
            #Kills the webcam window by executing the bash file 
            os.system("pkill zbarcam")

start_cam()
"""

p = os.popen('/usr/bin/zbarcam --prescale=300x300 --Sdisable -Sqrcode.enable', 'r')

def start_scan():
    global p
    while True:
        print('Scanning')
        data = p.readline()
        qrcode = str(data)[8:]
        if(qrcode):
            print(qrcode)

try:
    start_scan()
except KeyboardInterrupt:
    print('Stop scanning')
finally:
    p.close()
