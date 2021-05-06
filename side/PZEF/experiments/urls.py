from django.urls import path

from . import views

app_name = 'experiments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'opor/', views.OporView.as_view(), name='opor'),
]
