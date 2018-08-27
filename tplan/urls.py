from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProtocolHomeView.as_view(),name='home'),
    path('protocol/',views.ProtocolListView.as_view(),name='protocol_list'),
    path('protocol/<slug:slug>/',views.ProtocolDetailView.as_view(),name='protocol_detail'),
]