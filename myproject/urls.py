"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hello.views import MainpageView, DetailView, AddView, UpdateView, DeleteView

# app_name = "webapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', MainpageView.as_view(), name='home'),
    path('home/<int:pk>', DetailView.as_view(), name ='detail'),
    path('add/', AddView.as_view()),
    path('update/<int:pk>',UpdateView.as_view()),
    path('delete/<int:pk>',DeleteView.as_view()),
    path('accounts/', include('accounts.urls'))

]