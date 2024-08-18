from django.contrib.auth import get_user_model 
from django.test import TestCase

from .models import Expense

class ExpensesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser1",
            password="testpassword1234"
        )
        
        cls.expense = Expense.objects.create(
            title = "Test expense",
            description = "I'm just doing a test",
            amount = 0,
            user = cls.user,
            category = "Other",
        )
        
    def test_expense_model(self):
        self.assertEqual(self.expense.title, "Test expense")
        self.assertEqual(self.expense.description, "I'm just doing a test")
        self.assertEqual(self.expense.amount, 0)
        self.assertEqual(self.expense.user.username, "testuser1")
        self.assertEqual(self.expense.category, "Other")
        self.assertEqual(str(self.expense), "Test expense")