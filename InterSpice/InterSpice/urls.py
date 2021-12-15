"""InterSpice URL Configuration

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
from django.urls import path, include, re_path
from django.conf.urls import handler404, static, url
from django.conf import settings
from . import views

app_name = 'InterSpice'

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('album/', include('album.urls')),
    path('book/', include('book.urls')),
    path('article/', include('article.urls')),
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.page_not_found