from django.urls import path

from projetoDjango import views

urlpatterns = [
  path('', views.PostView.as_view(), name='home')
]