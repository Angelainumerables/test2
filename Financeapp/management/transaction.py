from django.test import TestCase
from django.urls import reverse
from Finance.Financeapp.models import Category, Transaction

class TransactionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Food', description='Grocery expenses')

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            category=self.category,
            amount=50.00,
            transaction_type='expense',
            description='Grocery shopping'
        )
        self.assertEqual(transaction.category, self.category)
        self.assertEqual(transaction.amount, 50.00)
        self.assertEqual(transaction.transaction_type, 'expense')
        self.assertEqual(transaction.description, 'Grocery shopping')

class TransactionViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Food', description='Grocery expenses')

    def test_transaction_create_view(self):
        response = self.client.post(reverse('transaction_create'), {
            'category': self.category,
            'amount': 100.00,
            'transaction_type': 'expense',
            'description': 'Dining out'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.first().description, 'Dining out')

    def test_transaction_update_view(self):
        transaction = Transaction.objects.create(
            category=self.category,
            amount=50.00,
            transaction_type='expense',
            description='Grocery shopping'
        )
        response = self.client.post(reverse('transaction_update', args=[transaction.pk]), {
            'category': self.category,
            'amount': 75.00,
            'transaction_type': 'expense',
            'description': 'Updated grocery shopping'
        })
        self.assertEqual(response.status_code, 302)
        transaction.refresh_from_db()
        self.assertEqual(transaction.amount, 75.00)
        self.assertEqual(transaction.description, 'Updated grocery shopping')

    def test_transaction_delete_view(self):
        transaction = Transaction.objects.create(
            category=self.category,
            amount=50.00,
            transaction_type='expense',
            description='Grocery shopping'
        )
        response = self.client.post(reverse('transaction_delete', args=[transaction.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Transaction.objects.count(), 0)

    def test_transaction_list_view(self):
        Transaction.objects.create(
            category=self.category,
            amount=50.00,
            transaction_type='expense',
            description='Grocery shopping'
        )
        response = self.client.get(reverse('transaction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grocery shopping')