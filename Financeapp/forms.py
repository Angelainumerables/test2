from django import forms
from .models import Category, Transaction, Budget, SavingGoal, Account

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'transaction_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'start_date', 'end_date']


class SavingGoalForm(forms.ModelForm):
    class Meta:
        model = SavingGoal
        fields = ['target_amount', 'current_amount', 'description', 'target_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account', 'balance']