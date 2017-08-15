from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormMixin
from django.core.urlresolvers import reverse_lazy

import asyncio

from .models import Settings, File
from .forms import FileForm
from django.conf import settings
import os

# Create your views here.

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }


@asyncio.coroutine
def zbar_scan():
    message = 'Get close QR code to cam'
    p=os.popen('/usr/bin/zbarcam --prescale=320x240','r')
    #Barcode variable read by Python from the commandline.

#    while True:
#        data = ""
            
#        while data == "":
            #print ("Data Antes de data = p.read..." % (data))
    data = p.readline()
            #print ("Data despu de data = p.read..." + (data))
            
    qrcode = str(data)[8:]
    if qrcode:
    #message = ("{0}".format(barcodedata))
        print(qrcode)
        message = qrcode
    #kill all running zbar tasks ... call from python
    #os.system("ps -face | grep zbar | awk '{print $2}' | xargs kill -s KILL")

    return {
    'cam'          : p,
    'message'   : message,
    }

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        eventloop = asyncio.new_event_loop()
        asyncio.set_event_loop(eventloop)
        eventloop.run_until_complete(zbar_scan()) 
        eventloop.close()			



class Setting(UpdateView):
    model = Settings
    template_name = "setting.html"
    success_url = reverse_lazy('home')
    fields = ['image_width', 'image_height', 'image_rotation', 'timeout']

class Game(TemplateView):
    template_name = "game.html"
#    os.popen('zbarcam --prescale=320x240')


def take_photo():
    global_settings = DBSession.query(Settigns).first()
    call (
            ['raspistill -t' + str(global_settings.timeout) +
            ' -w ' + str(global_settings.image_width) +
            ' -h ' + str(global_settings.image_height) +
            ' -rot ' + str(global_settings.image_rotation) +
            ' -o ' + "captura.jpg" ])
    return

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

