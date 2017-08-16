from django import template
import subprocess
import os

from appQRMusical import global_vars

register = template.Library()

@register.simple_tag
def start_cam():
	print ("Hola")
	print global_vars.message
"""
	if global_vars.zbar_status == None:
		global_vars.zbar_status = os.popen('/usr/bin/zbarcam --prescale=320x240','r')
"""

@register.simple_tag
def stop_cam():
	print("adios")
"""
	if global_vars.zbar_status != None:
		#Kills the webcam window by executing the bash file             
		os.system("ps -A | grep <application_name> | awk '{print $1}' | xargs kill -9 $1")
		global_vars.zbar_status = None
"""
