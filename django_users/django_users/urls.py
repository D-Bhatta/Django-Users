from django.urls import path

from django_users import views

app_name = "django_users"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
