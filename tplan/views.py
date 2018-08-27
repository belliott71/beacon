from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from .models import Protocol, Med, Lab, PreMed, PrnMed, Hydration
# Create your views here.

class ProtocolHomeView(ListView):

    model = Protocol

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    template_name = 'tplan/protocol_list.html'



class ProtocolListView(ListView):
    model = Protocol

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProtocolDetailView(DetailView):
    model = Protocol

    def get_queryset(self):
        return Protocol.objects.all()





