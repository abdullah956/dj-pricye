from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    #path/from hwere to load that/name of the function
]
