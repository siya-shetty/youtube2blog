from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Main app functionality
    path('main/', views.main, name='main'),  # GET page
    path('generate_blog/', views.generate_blog, name='generate_blog'),  # POST form submission
]
