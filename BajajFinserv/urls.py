from django.contrib import admin
from django.urls import path
from bfhl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bfhl/', views.evenoddarray),
]
