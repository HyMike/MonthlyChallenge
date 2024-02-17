from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("<int:months>", views.monthlyInt),
    path("<str:months>", views.monthly, name="months_path"),
]