from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Settings

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})

class Home(TemplateView):
    template_name = "home.html"

#class Setting(DetailView):
#    model = Settings
#    template_name = "setting.html"

class Setting(UpdateView):
    model = Settings
    template_name = "setting.html"
    success_url = reverse_lazy('home')
    fields = ['image_width', 'image_height', 'image_rotation', 'timeout']

class Upload(TemplateView):
    template_name = "upload.html"

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

