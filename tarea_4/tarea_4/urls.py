"""tarea_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from user_registration import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='registration/home_base2.html'), name='home'),
    path('user_profile/', TemplateView.as_view(template_name='UserProfile.html'), name='user_profile'),
    path('landing_page/', TemplateView.as_view(template_name='LandingPage.html'), name='landing_page'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('admin/', admin.site.urls),
    path('/', include('user_registration.urls')),
    path('/', include('django.contrib.auth.urls')),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^pass-success/$', TemplateView.as_view(template_name='change_password_success.html'), name='password_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
