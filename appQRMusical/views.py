from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Settings

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})

class Home(TemplateView):
    template_name = "home.html"

class Setting(DetailView):
    model = Settings
    template_name = "setting.html"

#    def get_context_data(self, **kwargs):
#        context = super(Setting, self).get_context_data(**kwargs)
#        context['setting'] = setting()
#        return context


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
