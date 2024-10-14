"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import index, login_view
from myapp import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/',views.signup),
    path('oshi/',views.oshi),
    path('hxh/',views.hxh),
    path('eva/',views.eva),
    path('stone/',views.stone),
    path('note/',views.note),

]
