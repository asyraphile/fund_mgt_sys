from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
#default urlpatterns for views or classview
urlpatterns = [
    # path('fund/', FundViewset.as_view(), name="Fund")
    #implementing django rest framework
    path('all/', views.get_all, name="Retrieve all funds"),
    path('fund/<uuid:id>/', views.get_fund, name="Retrieve all funds"),
    path('create/', views.create_fund, name="Create Fund"),
    path('update_performance/<uuid:id>/', views.update_performance_by_id, name="Update Performance by Id"),
    path('delete/<uuid:id>/', views.delete_fund_by_id, name="Delete Fund by Id"),
]
