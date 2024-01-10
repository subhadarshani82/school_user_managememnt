"""
URL configuration for djangoProject_college_management project.

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
from college_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard,name='dashboard'),
    path('role/', views.user_role,name='user_role'),
    path('add_user/', views.add_user,name='add_user'),
    path('all_user/', views.fetch_user,name='all_user'),
    path('teach/', views.teaching,name='teaching'),
    path('non_teach/', views.non_teaching,name='non_teach'),
    path('student/', views.student,name='student'),
    path('dlt_user/<int:id>/', views.delete_user,name='dlt_user'),
    path('get_user_data/<int:id>/', views.get_data_for_update_user,name='get_user_data'),
    path('update_user/<int:id>/', views.update_user,name='update_user'),
]
