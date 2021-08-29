from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('graph/', views.graph, name='graph'),
    path('graph/<int:days>/', views.graph, name='graph_by_days'),
    path('graph/<int:days>/<str:charttype>', views.graph, name='graph_by_days'),
]
