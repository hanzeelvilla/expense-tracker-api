from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Expense(models.Model):
    
    #CATEGORY CHOICES = {
        #"como se guarda en la bd", "como se muestra al usuario"
    #}
    
    CATEGORY_CHOICES = {
        "food": "Food",
        "transport": "Transport",
        "entretaiment": "Entretaiment",
        "health": "Health",
        "housing": "Housing",
        "education": "Education",
        "travel": "Travel",
        "gifts": "Gifts",
        "savings": "Savings",
        "pets": "Pets",
        "other": "Other", 
    }
    
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="OTHER", blank=False)
    created_at = models.DateField(blank=False)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title