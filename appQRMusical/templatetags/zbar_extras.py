from django import template
import subprocess
import os

from appQRMusical import global_vars

register = template.Library()

@register.simple_tag
def start_cam():
	print("Start Cam")
#	global_vars.cam = 0

@register.simple_tag
def stop_cam():
	print("Stop Cam")
"""
	if global_vars.zbar_status != None:
		#Kills the webcam window by executing the bash file             
		os.system("ps -A | grep zbar| awk '{print $1}' | xargs kill -9 $1")
		global_vars.zbar_status = None
"""
