import imp
from django.urls import path
from ads.views import index

urlpatterns = [
    path('', index)
]