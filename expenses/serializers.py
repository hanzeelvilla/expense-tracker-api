from rest_framework import serializers

from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "title",
            "description",
            "amount",
            "user",
            "category",
            "created_at",
            "updated_at"
        )
        model = Expense