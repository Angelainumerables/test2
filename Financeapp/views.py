from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CategoryForm, TransactionForm, BudgetForm, SavingGoalForm, AccountForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_transaction = Transaction.objects.filter(type__icontains=query)
        else:
            filtered_transaction = Transaction.objects.all()
        context['transaction'] = filtered_transaction
        context['total_transaction'] = Transaction.objects.all()
        context['total_category'] = Category.objects.count()
        context['total_amount'] = Amount.objects.count()
        context['total_date'] = Date.objects.count()
        context['total_description'] = Description.objects.count()
        return context

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

class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'app/budget_detail.html'
    context_object_name = 'budget'

    def get_queryset(self):
        return Budget.objects.all().order_by('-start_date')

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


def savinggoal_list(request):
    savinggoals = SavingGoal.objects.all()
    return render(request, 'app/savinggoal_list.html', {'savinggoals': savinggoals})

class SavingGoalDetailView(DetailView):
    model = SavingGoal
    template_name = 'app/savinggoal_detail.html'
    context_object_name = 'savinggoal'

    def get_queryset(self):
        return SavingGoal.objects.all().order_by('-target_date')

def savinggoal_create(request):
    if request.method == 'POST':
        form = SavingGoalForm(request.POST)
        if form.is_valid():
            savinggoal = form.save(commit=False)
            savinggoal.save()
            return redirect('savinggoal_list')
    else:
        form = SavingGoalForm()
    return render(request, 'app/savinggoal_form.html', {'form': form})

def savinggoal_update(request, pk):
    savinggoal = get_object_or_404(SavingGoal, pk=pk)
    if request.method == 'POST':
        form = SavingGoalForm(request.POST, instance=savinggoal)
        if form.is_valid():
            form.save()
            return redirect('savinggoal_list')
    else:
        form = SavingGoalForm(instance=savinggoal)
    return render(request, 'app/savinggoal_form.html', {'form': form})

def savinggoal_delete(request, pk):
    savinggoal = get_object_or_404(SavingGoal, pk=pk)
    if request.method == 'POST':
        savinggoal.delete()
        return redirect('savinggoal_list')
    return render(request, 'app/savinggoal_confirm_delete.html', {'savinggoal': savinggoal})


def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

def account_detail(request):
    account = get_object_or_404(Account, id=account-id)
    return render(request, 'account_detail.html', {'account': account})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
        return render(request, 'account_form.html', {'form': form})

def account_edit(request):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_detail', account_id=account.id)
    else:
        form = AccountForm(instance=account)
        return render(request, 'account_form.html', {'form': form})