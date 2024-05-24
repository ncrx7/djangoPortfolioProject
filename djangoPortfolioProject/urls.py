from django.contrib import admin
from django.urls import path
from .views import index
from .views import about
from.views import mygames
from .views import gallery
from .views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about.html', about, name='about'),
    path('mygames.html', mygames, name='mygames'),
    path('gallery.html', gallery, name='gallery'),
    path('contact.html', contact, name='contact'),
    path("index.html", index, name="index")
]