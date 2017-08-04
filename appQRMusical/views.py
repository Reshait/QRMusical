from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})

class Home(TemplateView):
    template_name = "home.html"

class Setting(TemplateView):
    template_name = "setting.html"

class Upload(TemplateView):
    template_name = "upload.html"

class Game(TemplateView):
    template_name = "game.html"
