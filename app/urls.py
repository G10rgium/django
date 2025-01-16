from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('donald', views.donald, name="donald"),
    path('log_in', views.log_in, name="log_in"),
    path('wendy', views.wendy, name="wendy"),
    path('tsisqvili', views.tsisqvili, name="tsisqvili"),
    path('kfc', views.kfc, name="kfc"),
    path('shawarma', views.shawarma, name="shawarma"),
    path('dunkin', views.dunkin, name="dunkin"),
    path('reg', views.reg, name="reg"),
]