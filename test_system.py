import unittest
import logging
from system import  Employee, HourlyEmployee, SalariedEmployee, Company


class Test_homework_3(unittest.TestCase):

    def setUp(self):
        self.employee_1 = HourlyEmployee(first_name="Ihor", last_name="Kozakov", role="CEO", amount=20)
        self.employee_2 = SalariedEmployee(first_name="Georg", last_name="Kirichenko", role="manager")
        self.employee_3 = HourlyEmployee(first_name="Olha", last_name="Okpenko", role="dev", amount=60)
        self.employees = [self.employee_1, self.employee_2, self.employee_3]
        self.company = Company(title='google', employees=self.employees)


    def test_company_init_(self):
        assert isinstance(self.company.title,str)
        assert isinstance(self.employees, list)

    def test_company_repr(self):
        assert repr(self.company) == "Company (title = google, employees = [HourlyEmployee(first_name='Ihor', last_name='Kozakov', role='CEO', vacation_days=25, amount=20, hourly_rate=50), SalariedEmployee(first_name='Georg', last_name='Kirichenko', role='manager', vacation_days=25, salary=5000), HourlyEmployee(first_name='Olha', last_name='Okpenko', role='dev', vacation_days=25, amount=60, hourly_rate=50)])"

    def test_company_pay(self):
        msg = "INFO:root:Paying Ihor Kozakov hourly rate of 50.00 for 20 hours. Total: 1000.00"
        with self.assertLogs(self.company.pay(self.employee_1), level='INFO') as cm:
            logging.getLogger().info('Paying Ihor Kozakov hourly rate of 50.00 for 20 hours. Total: 1000.00')
            self.assertEqual(cm.output, [msg])
        msg = "INFO:root:Paying monthly salary of 5000.00 to Georg Kirichenko"
        with self.assertLogs(self.company.pay(self.employee_2), level='INFO') as cm:
            logging.getLogger().info('Paying monthly salary of 5000.00 to Georg Kirichenko')
            self.assertEqual(cm.output, [msg])