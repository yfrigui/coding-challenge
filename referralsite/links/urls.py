from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/', views.click, name='click'),
    path('link-input/', views.add_link, name='add_link'),
    path('delete/', views.delete_link, name='delete_link'),
    path('edit/', views.begin_edit_link, name='begin_edit_link'),
    path('finish-edit/', views.finish_edit_link, name='finish_edit_link')
]