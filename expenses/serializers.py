from rest_framework import serializers
from django.utils import timezone

from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "amount",
            "category",
            "created_at",
            "updated_at"
        )
        model = Expense
    
    #If the user doesn't provide a date    
    def validate_created_at(self, value):
        return value or timezone.now().date()