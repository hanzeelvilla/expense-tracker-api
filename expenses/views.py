from rest_framework import generics

from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import isOwner

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [isOwner]