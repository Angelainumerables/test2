from django.contrib import admin
from .models import Category, Transaction, Budget, SavingGoal, Account

admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(SavingGoal)
admin.site.register(Account)