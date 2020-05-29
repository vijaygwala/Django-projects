"""schoolproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from schoolapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Schoolbs/', views.Schoolbs),
    url(r'^Aboutus/', views.Aboutus),
    url(r'^Transfer/', views.Transfer),
    url(r'^Contactus/', views.Contactus),
    url(r'^Gallary/', views.Gallary),
    url(r'^Message/', views.Message),
    url(r'^Facilities/', views.Facilities),
    url(r'^Notice/', views.Notice),
    url(r'^Dbtable/', views.dbtable),
    


]
urlpatterns=urlpatterns +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
