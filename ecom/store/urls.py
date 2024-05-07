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
    path('register/',views.register_user,name='register'),
    path('update_user/',views.update_user,name='update_user'),
    path('product/<int:pk>',views.product,name='product'),
    #int pk means integer primary key
    path('category/<str:foo>', views.category, name='category'),
    #catagory will be name and foo is jsut a placeholder 
    path('category_summary/', views.category_summary, name='category_summary'),

]
