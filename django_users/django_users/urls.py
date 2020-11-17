from django.urls import include, path

from django_users import views

app_name = "django_users"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]
