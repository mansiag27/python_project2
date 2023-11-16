from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from django.db.models import Sum
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()
    total_expense = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_expense': total_expense,
    })

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'expenses/expense_detail.html', {'expense': expense})

def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_edit.html', {'form': form})

def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_edit.html', {'form': form})

def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expense_list')


# Create your views here.
