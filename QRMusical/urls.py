"""QRMusical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appQRMusical import views
from django.conf import settings
from django.conf.urls.static import static

from appQRMusical.views import Setting, Game, Item_detail, Item_delete
#from appQRMusical.views import Upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^$', Home.as_view(), name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^$', views.message, name='message'),
    url(r'^setting/(?P<pk>\d+)/$', Setting.as_view(), name='setting'),

    url(r'^upload/$', views.upload, name ='upload'),
#    url(r'^upload/$', views.last_items, name ='last_items'),

    url(r'^game/$', Game.as_view(), name = 'game'),
    url(r'^item_detail/(?P<pk>\d+)/$', Item_detail.as_view(), name='item_detail'),
    url(r'^item_list/$', views.item_list, name='item_list'),
    url(r'^item_detail/(?P<pk>\d+)/delete/$', Item_delete.as_view(), name='item_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
