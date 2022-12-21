"""payment_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from versionedapi.v2.router import api_urlpatterns as api_v2
#from payment_api.urls import 

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'api/v1/', include("payments.urls")),
    path("users/", include("users.urls")),
    re_path(r'^api/v2/', include(api_v2)),
]
