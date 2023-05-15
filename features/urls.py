from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendfeedback, name='sendfeedback'),
    path('ViewFeedbacks', views.viewfeedback, name='viewfeedback')
]