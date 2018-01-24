from django.urls import include, path
from django.contrib import admin

urlpatterns = [
	path('',include('nqg.urls')),
    path('nqg/', include('nqg.urls')),
    path('nqg2/', include('nqg.urls')),
    path('nqg/genq/', include('nqg.urls')),

]