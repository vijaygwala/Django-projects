"""MyAccounts URL Configuration

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
from accounts import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^UserHome/',views.UserHome,name='UserHome'),
    url(r'^Product/',views.Products,name='Product'),
    url(r'^Customer/(?P<pk>\d+)/$', views.Customers,name='Customer'),
    url(r'^Status', views.Status),
    url(r'^Dash/', views.Dash,name='Dash'),
    url(r'^order_form/(?P<pk>\d+)/$', views.createOrder,name='order_form'),
    url(r'^update_order/(?P<pk>\d+)/$', views.updateOrder,name='update_order'),
    url(r'^delete_order/(?P<pk>\d+)/$', views.deleteOrder,name='delete_order'),
    #path('Customer/<str:pk_test>/', views.Customers,name='Customer'),
    url(r'^registerPage/', views.registerPage,name='registerPage'),
    url(r'^Login/', views.Login,name='Login'),
    url(r'^Logout/', views.Logout,name='Logout'),
    url(r'^AccountProfile/', views.AccountProfile,name='AccountProfile'),

    url(r'^reset_password/', auth_views.PasswordResetView.as_view(),name='reset_password'),
    url(r'^reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
