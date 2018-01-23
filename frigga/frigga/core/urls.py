from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name='index'),

    path('fund/add', views.funds, name='funds'),
    path('unit/add', views.units, name='units'),
    path('specie/add', views.species, name='species'),
]

