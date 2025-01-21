from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('transactions/', views.TransactionPage, name='transaction'),
    path('transaction/', views.transaction_list, name='transaction'),
    path('transaction/create/', views.transaction_create, name='transaction_create'),
    path('transactions/update/<int:pk>/', views.transaction_update, name='transaction_update'),
    path('transactions/delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),

    path('budget/', views.budget_list, name='budget_list'),
    path('budget/', views.budget_list, name='budget'),
    path('budgets/create/', views.budget_create, name='budget_create'),
    path('budgets/update/<int:pk>/', views.budget_update, name='budget_update'),
    path('budgets/delete/<int:pk>/', views.budget_delete, name='budget_delete'),
]