from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Settings, File
from .forms import FileForm
from django.conf import settings
import os
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Setting(UpdateView):
    model = Settings
    template_name = "setting.html"
    success_url = reverse_lazy('home')
    fields = ['image_width', 'image_height', 'image_rotation', 'timeout']

class Game(TemplateView):
    template_name = "game.html"

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
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'upload.html', {
        'form': form
    })

"""
def upload(request):
    output_list = os.popen('ls').read()
    output_list = output_list.splitlines()

    if request.method == 'POST' and request.FILES['myfile']:
       
        myfile = request.FILES['myfile']

        if myfile.name.endswith('.mp3'):
            uploaded_file_url = os.path.join(settings.MEDIA_ROOT, 'sounds/')
        elif myfile.name.endswith('.jpg'):
            uploaded_file_url = os.path.join(settings.MEDIA_ROOT, 'images/')
        else:
            uploaded_file_url = fs.url(filename)

        fs = FileSystemStorage(location = uploaded_file_url)
        filename = fs.save(myfile.name, myfile)

        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url, 'output_list': output_list})
    return render(request, 'upload.html', {'output_list': output_list})
"""
