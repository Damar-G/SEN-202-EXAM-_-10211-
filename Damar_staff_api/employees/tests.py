from django.test import TestCase
from .models import Manager, Intern

class ManagerModelTest(TestCase):
    def setUp(self):
        self.manager = Manager.objects.create(
            name="John Doe",
            department="Sales",
            has_company_card=True
        )

    def test_manager_creation(self):
        self.assertEqual(self.manager.name, "John Doe")
        self.assertEqual(self.manager.department, "Sales")
        self.assertTrue(self.manager.has_company_card)

    def test_get_role(self):
        self.assertEqual(self.manager.get_role(), "Manager")

class InternModelTest(TestCase):
    def setUp(self):
        self.manager = Manager.objects.create(
            name="Jane Smith",
            department="Marketing",
            has_company_card=True
        )
        self.intern = Intern.objects.create(
            name="Alice Johnson",
            mentor=self.manager,
            internship_end="2023-12-31"
        )

    def test_intern_creation(self):
        self.assertEqual(self.intern.name, "Alice Johnson")
        self.assertEqual(self.intern.mentor, self.manager)
        self.assertEqual(str(self.intern.internship_end), "2023-12-31")

    def test_get_role(self):
        self.assertEqual(self.intern.get_role(), "Intern")