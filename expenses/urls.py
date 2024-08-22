from django.urls import path

from .views import ExpenseList, ExpenseDetail, ExpenseTotal

urlpatterns = [
    path("total/", ExpenseTotal.as_view(), name="expense_total"),
    path("<int:pk>/", ExpenseDetail.as_view(), name="expense_detail"),
    path("", ExpenseList.as_view(), name="expense_list"),
]
