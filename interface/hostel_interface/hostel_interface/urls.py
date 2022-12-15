"""hostel_interface URL Configuration

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

from django.urls import path, include
from interface import views


#from rest_framework.routers import DefaultRouter
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    #path('admin', admin.site.urls),
    #path('auth/', include('auth.urls')),
    #path('api-auth/', include('rest_framework.urls')),

    path('', views.index),
    path('index.html', views.index),
    path('add-booking.html/', views.add_booking),
    path('all-booking.html/', views.all_booking),
    path('all-customer.html/', views.all_customer),
    path('all-customer/<int:id>', views.del_customer),
    path('all-rooms.html/', views.all_room),
    path('add-room.html/', views.add_room),
    path('edit-customer/<int:id>', views.edit_customer),

    path('add-placetype.html', views.add_placetype),
    path('placetypes.html', views.all_placetype),

    path('services.html', views.all_services),
    path('add-service.html', views.add_service),
    path('reviews.html/', views.get_reviews),

    path('login.html', views.login),
    path('post-login-user-index.html', views.postLoginUser),
    path('post-login-admin-index.html', views.postLoginAdmin),

    path('user-add-booking.html/', views.user_add_booking),
    path('user-all-rooms.html/', views.user_all_room),
    path('user-placetypes.html', views.user_all_placetype),
    path('user-services.html', views.user_all_services),

]


