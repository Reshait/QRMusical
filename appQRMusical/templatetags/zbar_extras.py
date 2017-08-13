from django import template
import subprocess

import os

register = template.Library()

@register.simple_tag
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


@register.simple_tag
def stop_cam():
        #Kills the webcam window by executing the bash file             
        os.system("pkill zbarcam")
