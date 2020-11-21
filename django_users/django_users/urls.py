from django.urls import include, path

from django_users import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]
