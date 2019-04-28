from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
path('', views.home),
path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
path('logout/', LogoutView.as_view(template_name='account/logout.html'), name="logout"),
path('register/', views.register, name = 'register'),
path('profile/', views.view_profile, name='view_profile'),   # this will show the users information
path('profile/edit/', views.edit_profile, name='edit_profile'),
path('change_password/', views.change_password, name='change_password'),
path('workstations1/', views.workstations1, name='workstations1'),
path('workstations2/', views.workstations2, name='workstations2'),
path('about/', views.about, name= 'about'),

path('workstations2/experiment1/', views.experiment1, name='experiment1'),
path('workstations2/experiment2/', views.experiment2, name='experiment2'),
path('workstations2/experiment3/', views.experiment3, name='experiment3'),
path('workstations1/experiment1/', views.experiment1, name='experiment1'),
path('workstations1/experiment2/', views.experiment2, name='experiment2'),
path('workstations1/experiment3/', views.experiment3, name='experiment3'),
path('workstations2/about', views.about, name='about'), 
path('workstation1/experiment1/media/', views.media, name='media'), 

path('workstation1/home/', views.back_home, name='back_home'),

]