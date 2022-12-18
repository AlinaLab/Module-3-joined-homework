import unittest
import logging
from system import Employee, HourlyEmployee, SalariedEmployee, Company


class TestSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.first_name1 = "Ihor"
        self.last_name1 = "Kozakov"
        self.first_name2 = "Georg"
        self.last_name2 = "Kirichenko"
        self.first_name3 = "Olha"
        self.last_name3 = "Okpenko"
        self.role1 = 'CEO'
        self.role2 = 'manager'
        self.role3 = 'dev'
        self.vacation_days = 25
        self.amount3 = 60
        self.hourly_rate = 50
        self.salary = 5000
        self.employee1 = HourlyEmployee(self.first_name1, self.last_name1, self.role1)
        self.employee2 = SalariedEmployee(self.first_name2, self.last_name2, self.role2)
        self.employee3 = HourlyEmployee(self.first_name3, self.last_name3, self.role3, self.amount3)
        self.employees = [self.employee1, self.employee2, self.employee3]
        self.company = Company(title='google', employees=self.employees)

    def test_init(self):
        self.assertEqual(
            (self.employee1.first_name, self.employee1.last_name, self.employee1.role, self.employee1.vacation_days),
            (str(self.first_name1), str(self.last_name1), str(self.role1), int(self.vacation_days)))
        self.assertEqual((self.employee2.first_name, self.employee2.last_name, self.employee2.role,
                          self.employee2.vacation_days, self.employee2.salary),
                         (str(self.first_name2), str(self.last_name2), str(self.role2), int(self.vacation_days),
                          int(self.salary)))
        self.assertEqual((self.employee3.first_name, self.employee3.last_name, self.employee3.role,
                          self.employee3.amount, self.employee1.vacation_days),
                         (str(self.first_name3), str(self.last_name3), str(self.role3), 0, int(self.vacation_days)))

    def test_full_name(self):
        self.assertEqual(self.employee1.fullname, self.first_name1 + ' ' + self.last_name1)
        self.assertEqual(self.employee2.fullname, self.first_name2 + ' ' + self.last_name2)
        self.assertEqual(self.employee3.fullname, self.first_name3 + ' ' + self.last_name3)

    def test__str__(self):
        self.assertEqual(self.employee1.fullname, 'Ihor Kozakov')
        self.assertEqual(self.employee2.fullname, 'Georg Kirichenko')
        self.assertEqual(self.employee3.fullname, 'Olha Okpenko')

    def test_log_work(self):
        self.assertEqual(self.employee1.amount, 0)
        self.assertEqual(self.employee3.amount, 0)

    def test_obj_instance(self):
        self.assertIsInstance(self.employee1, HourlyEmployee)
        self.assertIsInstance(self.employee2, SalariedEmployee)
        self.assertIsInstance(self.employee3, HourlyEmployee)

    def test_take_holiday(self):
        self.assertEqual(self.employee2.take_holiday(True), None)
        self.assertEqual(self.employee1.take_holiday(False), None)

    def test_company_init_(self):
        assert isinstance(self.company.title, str)
        assert isinstance(self.employees, list)

    def test_company_str(self) -> None:
        self.assertEqual(self.company.title, 'google')

    def test_company_repr(self):
        assert repr(self.company) == "Company (title = google, employees = [HourlyEmployee(first_name='Ihor', last_name='Kozakov', role='CEO', vacation_days=25, amount=20, hourly_rate=50), SalariedEmployee(first_name='Georg', last_name='Kirichenko', role='manager', vacation_days=25, salary=5000), HourlyEmployee(first_name='Olha', last_name='Okpenko', role='dev', vacation_days=25, amount=60, hourly_rate=50)])"

    def test_company_add_to_company(self):
        """Тест на перевірку чи додає функція до списку працівників компанії"""

        self.employees.append(self.employee1)
        self.employees.append(self.employee2)
        self.employees.append(self.employee3)
        self.assertIn(self.employee1, self.employees)
        self.assertIn(self.employee2, self.employees)
        self.assertIn(self.employee3, self.employees)

    def test_get_ceos(self):
        """Tests get_ceos method"""

        self.assertEqual(['Ihor Kozakov'], self.company.get_ceos())

    def test_get_managers(self):
        """"Tests get_managers method """

        self.assertEqual(['Georg Kirichenko'], self.company.get_managers())

    def test_get_developers(self):
        """Test get_developers method"""

        self.assertEqual(['Olha Okpenko'], self.company.get_developers())

    def test_company_pay(self):
        msg = "INFO:root:Paying Ihor Kozakov hourly rate of 50.00 for 20 hours. Total: 1000.00"
        with self.assertLogs(self.company.pay(self.employee1), level='INFO') as cm:
            logging.getLogger().info('Paying Ihor Kozakov hourly rate of 50.00 for 20 hours. Total: 1000.00')
            self.assertEqual(cm.output, [msg])
        msg = "INFO:root:Paying monthly salary of 5000.00 to Georg Kirichenko"
        with self.assertLogs(self.company.pay(self.employee2), level='INFO') as cm:
            logging.getLogger().info('Paying monthly salary of 5000.00 to Georg Kirichenko')
            self.assertEqual(cm.output, [msg])

    def test_company_pay_all(self):
        """Тест на перевірку чи повертає функція інформацію по усім працівникам компанії одночасно"""

        self.assertEqual(self.company.pay(self.employee1), None)
        self.assertEqual(self.company.pay(self.employee2), None)
        self.assertEqual(self.company.pay(self.employee3), None)

