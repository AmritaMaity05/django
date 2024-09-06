from django.contrib import admin
from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    re_path(r'^student$', views.studentApi),           # For handling requests to /student
    re_path(r'^student/([0-9]+)$', views.studentApi),  # For handling requests to /student/<id>
    path('admin/', admin.site.urls),                   # Admin panel
]
