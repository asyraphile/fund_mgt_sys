from django.urls import path
from . import views
from .views import FundViewset
from rest_framework.routers import DefaultRouter
#default urlpatterns for views or classview
urlpatterns = [
    path('fund/', FundViewset.as_view(), name="Fund")
    #implementing django rest framework
    #path('all/', views.all_funds, name="Retrieve all funds"),
    #path('all/', views.all_funds, name="Retrieve all funds"),
]
router = DefaultRouter()
router.register('fund', views.FundViewset, basename='fund')
urlpatterns += router.urls