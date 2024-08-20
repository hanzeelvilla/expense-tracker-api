from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import isOwner

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "title": ["exact"],
        "category": ["exact"],
        "amount": ["exact", "gt", "lt"],  # Añadimos los filtros de rangos
        "created_at": ["exact", "gte", "lte"],
        "updated_at": ["exact", "gte", "lte"],
    }
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [isOwner]