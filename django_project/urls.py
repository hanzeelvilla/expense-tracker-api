from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", include("authorization.urls")),
    path("api/expenses/", include("expenses.urls"))
]
