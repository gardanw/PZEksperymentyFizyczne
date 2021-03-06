from django.urls import path

from . import views

app_name = 'experiments'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'opor/', views.OporView.as_view(), name='opor'),
    path(r'pocisk/', views.PociskView.as_view(), name='pocisk'),
    path(r'mrowki/', views.MrowkiView.as_view(), name='mrowki'),
    path(r'wektory/', views.WektoryView.as_view(), name='wektory'),
    path(r'ncial/', views.NCialView.as_view(), name='ncial'),
    path(r'smok/', views.SmokView.as_view(), name='smok'),
]
