from django.urls import path
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
#default urlpatterns for views or classview
urlpatterns = [
    path('fund/',)
    #implementing django rest framework
    #path('all/', views.all_funds, name="Retrieve all funds"),
    #path('all/', views.all_funds, name="Retrieve all funds"),
]
router = DefaultRouter()
router.register('fund',)