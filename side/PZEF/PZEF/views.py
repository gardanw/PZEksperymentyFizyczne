from django.views import generic
from experiments.models import Eksperymenty

class HomePage(generic.ListView):
    template_name = 'experiments/home.html'
    context_object_name = 'eksperymenty'

    def get_queryset(self):
        return Eksperymenty.objects.order_by('exp_name')


class OprojekcieView(generic.ListView):
    template_name = 'experiments/oprojekcie.html'
    context_object_name = 'eksperymenty'

    def get_queryset(self):
        return Eksperymenty.objects.order_by('exp_name')