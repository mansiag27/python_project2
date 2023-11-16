# expenses/urls.py
from django.urls import path
from .views import expense_list, expense_detail, expense_new, expense_edit, expense_delete

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('<int:pk>/', expense_detail, name='expense_detail'),
    path('new/', expense_new, name='expense_new'),
    path('<int:pk>/edit/', expense_edit, name='expense_edit'),
    path('<int:pk>/delete/', expense_delete, name='expense_delete'),
]
