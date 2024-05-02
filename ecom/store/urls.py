from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    #path/from hwere to load that/name of the function
    #jsut like the webp in laravel
    path('about/',views.about,name='about'),
    # for each page u need template  view and url 
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
