"""recipe_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import login
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', login),
    path('', include('recipe_app.recipe.urls')),
    path('docs/', include_docs_urls(title='My Recipe API ',permission_classes=[AllowAny,])),
    # path('', RedirectView.as_view(url='docs/')),
]
