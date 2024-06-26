"""
URL configuration for diabetic project.

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
# from django.contrib import admin
# from django.urls import path
# from . import views
# from .views import predict, form_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.diabetics),
#     path('predict/', predict, name='predict'),
#     path('form/', form_view, name='form'),
# ]


# diabetes_project/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import diabetics_home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', diabetics_home, name='diabetics_home'),
    path('predict/', include('prediction.urls')),
]

urlpatterns+=staticfiles_urlpatterns()