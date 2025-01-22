from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CategoryForm, TransactionForm, BudgetForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def HomePage(request):
    return render(request, 'app/home.html')

def TransactionPage(request):
    transactions = Transaction.objects.all()
    return render(request, 'app/transaction_list.html')

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'app/transaction_list.html', {'transactions': transactions})

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'app/transaction_detail.html'
    context_object_name = 'transaction'

    def get_queryset(self):
        return Transaction.objects.all().order_by('-date')

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction')
    else:
        form = TransactionForm()
    return render(request, 'app/transaction_form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'app/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction')
    return render(request, 'app/transaction_confirm_delete.html', {'transaction': transaction})

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'app/budget_list.html', {'budgets': budgets})

def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'app/budget_form.html', {'form': form})

def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'app/budget_form.html', {'form': form})

def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'app/budget_confirm_delete.html', {'budget': budget})