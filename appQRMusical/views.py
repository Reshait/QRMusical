from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormMixin
from django.core.urlresolvers import reverse_lazy

import threading

from .models import Settings, File
from .forms import FileForm
from django.conf import settings
import os

import global_vars

# Create your views here.
"""
def get_current_path(request):
	return {
	   'current_path': request.get_full_path()
	 }
"""
	
def message(request):
	global_vars.message
	context = {'glob_message' : global_vars.message,}
	return render(request, 'glob_message.html', context)

"""	
def capturar():
	global p
"""

def home(request):	
	global_vars.cam
	global_vars.message
	global_vars.zbar_status
	
	if global_vars.cam == 0:
		global_vars.message = 'Get close QR code to cam'
		global_vars.cam = 1

	elif global_vars.cam == 1:
		global_vars.zbar_status = os.popen('/usr/bin/zbarcam --prescale=320x240','r')
		global_vars.cam = 2
		
	elif global_vars.cam == 2:
		data = global_vars.zbar_status.readline()
		qrcode = str(data)[8:]
		if qrcode:
			print(qrcode)
			global_vars.message = qrcode

	print(global_vars.message)

	context = {'message' : global_vars.message,}
	return render(request, 'home.html', context)

class Setting(UpdateView):
	model = Settings
	template_name = "setting.html"
	success_url = reverse_lazy('home')
	fields = ['image_width', 'image_height', 'image_rotation', 'timeout']

class Game(TemplateView):
	template_name = "game.html"

"""
def take_photo():
	global_settings = DBSession.query(Settigns).first()
	call (
			['raspistill -t' + str(global_settings.timeout) +
			' -w ' + str(global_settings.image_width) +
			' -h ' + str(global_settings.image_height) +
			' -rot ' + str(global_settings.image_rotation) +
			' -o ' + "captura.jpg" ])
	return
"""

def upload(request):
	images_list = File.objects.order_by('-upload_date').filter(filetype="jpg")[:5]
	songs_list  = File.objects.order_by('-upload_date').filter(filetype="mp3")[:5]
	sounds_list = File.objects.order_by('-upload_date').filter(filetype="ogg")[:5]

	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			file_up = File()
			file_up.file = request.FILES['file']
			file_up.filename = request.FILES['file'].name
			name, ext = file_up.filename.rsplit('.', 1)
			file_up.filetype = ext
			file_up.save()
			return redirect('upload')
	else:
		form = FileForm()

	return render(request, 'upload.html', {
		'form'          : form,
		'images_list'   : images_list,
		'songs_list'    : songs_list,
		'sounds_list'   : sounds_list
	})

