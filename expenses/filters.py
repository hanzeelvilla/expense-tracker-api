import django_filters

from .models import Expense

class ExpenseListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="exact")
    category = django_filters.CharFilter(field_name="category", lookup_expr="exact")
    amount = django_filters.NumberFilter(field_name="amount", lookup_expr="exact")
    min_amount = django_filters.NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = django_filters.NumberFilter(field_name="amount", lookup_expr="lte")
    date = django_filters.DateFilter(field_name="created_at", lookup_expr="exact")
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
    update = django_filters.DateFilter(field_name="updated_at", lookup_expr="exact")
    start_update = django_filters.DateFilter(field_name="updated_at", lookup_expr="gte")
    end_update = django_filters.DateFilter(field_name="updated_at", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = [
            "title",
            "category",
            "amount",
            "max_amount",
            "min_amount",
            "date",
            "start_date",
            "end_date",
            "update",
            "start_update",
            "end_update"
        ]

class TotalExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")
    category = django_filters.CharFilter(field_name="category", lookup_expr="exact")
    
    class Meta:
        model = Expense
        fields = ["start_date", "end_date", "category"]