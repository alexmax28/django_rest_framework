"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from musics.views import hello_view
from project1.testdb import add, gall, update, delete
# import project1.testdb
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from rest_framework.routers import DefaultRouter
from musics import views

schema_view = get_swagger_view(title='API')

router = DefaultRouter()
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # # path('hello/', hello_view),
    # # path('add/$', add),
    # re_path('add$', add),
    # path('gall/', gall),
    # re_path('update$', update),
    # re_path('del$', delete),
    # path('docs/', schema_view),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
