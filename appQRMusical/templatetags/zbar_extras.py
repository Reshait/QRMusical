from django import template
import os

register = template.Library()

def zbar_activate():
	cam=os.popen('/usr/bin/zbarcam --prescale=320x240', 'r')
	while True:
	    code = cam.readline()
	    print 'Got barcode:' , code