from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_name, name="get_name"),
    path('genq/',views.get_name,name="get_name"),
    path('genq2',views.get_name_par, name='paragraph'),
    path('genq/file/',views.upload_fle, name='upload_fle'),
]