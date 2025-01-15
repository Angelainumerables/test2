from django.test import TestCase
from django.urls import reverse
from Finance.Financeapp.models import Budget, Category

class BudgetModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Savings', description='Savings category')

    def test_budget_creation(self):
            amount=1000.00,
            start_date='2023-01-01',
            end_date='2023-12-31'
        )
        self.assertEqual(budget.user, self.user)
        self.assertEqual(budget.amount, 1000.00)
        self.assertEqual(budget.start_date.strftime('%Y-%m-%d'), '2023-01-01')
        self.assertEqual(budget.end_date.strftime('%Y-%m-%d'), '2023-12-31')

class BudgetViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Savings', description='Savings category')

    def test_budget_create_view(self):
        response = self.client.post(reverse('budget_create'), {
            'amount': 1500.00,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertEqual(Budget.objects.count(), 1)
        self.assertEqual(Budget.objects.first().amount, 1500.00)

    def test_budget_update_view(self):
        budget = Budget.objects.create(
            amount=1000.00,
            start_date='2023-01-01',
            end_date='2023-12-31'
        )
        response = self.client.post(reverse('budget_update', args=[budget.pk]), {
            'amount': 2000.00,
            'start_date': '2023-01-01',
            'end_date': '2023-12-31'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        budget.refresh_from_db()
        self.assertEqual(budget.amount, 2000.00)

    def test_budget_delete_view(self):
        budget = Budget.objects.create(
            amount=1000.00,
            start_date='2023-01-01',
            end_date='2023-12-31'
        )
        response = self.client.post(reverse('budget_delete', args=[budget.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertEqual(Budget.objects.count(), 0)

    def test_budget_list_view(self):
        Budget.objects.create(
            amount=1000.00,
            start_date='2023-01-01',
            end_date='2023-12-31'
        )
        response = self.client.get(reverse('budget_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1000.00')