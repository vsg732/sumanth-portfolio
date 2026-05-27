# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.admin_page, name='admin'),
    path('', views.portfolio, name='portfolio'),
]
