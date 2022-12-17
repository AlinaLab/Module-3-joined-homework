import unittest
from system import Employee, HourlyEmployee, SalariedEmployee, Company

class Test_Company(unittest.TestCase):

    def setUp(self):
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
        self.emploee1 = HourlyEmployee(self.first_name1, self.last_name1, self.role1)
        self.emploee2 = SalariedEmployee(self.first_name2, self.last_name2, self.role2)
        self.emploee3 = HourlyEmployee(self.first_name3, self.last_name3, self.role3, self.amount3)
        employees = [self.emploee1, self.emploee2, self.emploee3]
        self.company = Company(title='google', employees= employees)


    def test_get_ceos(self):
        """Tests get_ceos method"""

        self.assertEqual(['Ihor Kozakov'], self.company.get_ceos())
    
    def test_get_managers(self):
        """"Tests get_managers method """

        self.assertEqual(['Georg Kirichenko'], self.company.get_managers())

    def test_get_developers(self):
        """Test get_developers method"""

        self.assertEqual(['Olha Okpenko'], self.company.get_developers())

if __name__ == '__main__':
    unittest.main()