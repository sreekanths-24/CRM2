from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendfeedback, name='sendfeedback'),
    path('ViewFeedbacks', views.viewfeedback, name='viewfeedback'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('ecommdata', views.ecommdata, name='ecommdata'),
    path('ecommorderdata', views.ecommorderdata, name='ecommorderdata'),
]