from django.urls import path

from .views import ExpenseList, ExpenseDetail

urlpatterns = [
    path("<int:pk>/", ExpenseDetail.as_view(), name="expense_detail"),
    path("", ExpenseList.as_view(), name="expense_list"),
]
