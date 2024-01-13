# cleaning_company_project/urls.py
from django.urls import path, include
from . import views 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import BlogDetailView, BlogsListView, add_comment
from django.contrib import admin
from chole_cleaners.views import home, services, contact, about_us, careers, tenders, blogs, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('aboutus/', about_us, name='aboutus'),
    path('careers/', careers, name='careers'),
    path('tenders/', tenders, name='tenders'),
    path('blogs/', blogs, name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:blog_id>/add_comment/', add_comment, name='add_comment'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]


