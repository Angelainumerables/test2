from django.urls import path
from . import views
from .views import TransactionDetailView, BudgetDetailView, SavingGoalDetailView, account_detail

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('transactions/', views.TransactionPage, name='transaction'),
    path('transaction/', views.transaction_list, name='transaction_list'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transaction/create/', views.transaction_create, name='transaction_create'),
    path('transactions/update/<int:pk>/', views.transaction_update, name='transaction_update'),
    path('transactions/delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),

    path('budget/', views.budget_list, name='budget_list'),
    path('budget/', views.budget_list, name='budget'),
    path('budget/<int:pk>/', BudgetDetailView.as_view(), name='budget_detail'),
    path('budgets/create/', views.budget_create, name='budget_create'),
    path('budgets/update/<int:pk>/', views.budget_update, name='budget_update'),
    path('budgets/delete/<int:pk>/', views.budget_delete, name='budget_delete'),

    path('savinggoal/', views.savinggoal_list, name='savinggoal_list'),
    path('savinggoal/', views.savinggoal_list, name='savinggoal'),
    path('savinggoal/<int:pk>/', SavingGoalDetailView.as_view(), name='savinggoal_detail'),
    path('savinggoals/create/', views.savinggoal_create, name='savinggoal_create'),
    path('savinggoals/update/<int:pk>/', views.savinggoal_update, name='savinggoal_update'),
    path('savinggoals/delete/<int:pk>/', views.savinggoal_delete, name='savinggoal_delete'),


    path('', views.account_list, name='account_list'),
    path('account/<int:account_id>/', views.account_detail, name='account_detail'),
    path('account/create/', views.account_create, name='account_create'),
    path('account/edit/<int:account_id>/', views.account_edit, name='account_edit')
]