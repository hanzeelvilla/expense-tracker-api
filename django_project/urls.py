from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("authorization.urls")),
    path("api/expenses/", include("expenses.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/documentation/", SpectacularRedocView.as_view(), name="redoc"),
]
