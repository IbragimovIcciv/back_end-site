from django.urls import path
from .views import HomeView, LoginView, contact, ProductView, AboutView, RegisterView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('product', ProductView.as_view(), name='product'),
    path('contact', contact, name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),

]
