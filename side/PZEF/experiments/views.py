from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Eksperymenty


class IndexView(generic.ListView):
    template_name = 'experiments/index.html'
    context_object_name = 'eksperymenty'

    def get_queryset(self):
        return Eksperymenty.objects.order_by('exp_name')


class OporView(generic.edit.CreateView):
    template_name = 'experiments/opor.html'
    form_class = UserCreationForm
