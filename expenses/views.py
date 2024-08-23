from rest_framework import generics
from django.db.models import Sum
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import isOwner
from .filters import ExpenseListFilter, TotalExpenseFilter

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ExpenseListFilter
    ordering_fields = ("amount", "created_at")
    ordering = ("created_at",)
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [isOwner]

class ExpenseTotal(generics.GenericAPIView):
    filter_backends = [DjangoFilterBackend]   
    filter_class = TotalExpenseFilter
    
    def get(self, request, *args, **kwargs):
        filtered_expenses = TotalExpenseFilter(request.query_params, queryset=Expense.objects.filter(user=request.user)).qs
        total = filtered_expenses.aggregate(Sum("amount", default=0))
        
        return Response({"total": total["amount__sum"]})