from django.contrib.auth.models import User
from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = {
        "FOOD": "Food",
        "TRANSPORT": "Transport",
        "ENTRETAIMENT": "Entretaiment",
        "HEALTH": "Health",
        "HOUSING": "Housing",
        "EDUCATION": "Education",
        "TRAVEL": "Travel",
        "GIFTS": "Gifts",
        "SAVINGS": "Savings",
        "PETS": "Pets",
        "OTHER": "Other", 
    }
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="OTHER")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title