from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path(r'admin<admin_id>/', admin_panel),
    path('result_page/', send_results)
]
