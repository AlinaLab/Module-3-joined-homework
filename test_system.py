import unittest
from system import Employee, HourlyEmployee, SalariedEmployee


class Test_system(unittest.TestCase):
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
            self.emploee1 = HourlyEmployee(self.first_name1, self.last_name1, self.role1)
            self.emploee2 = SalariedEmployee(self.first_name2, self.last_name2, self.role2)
            self.emploee3 = HourlyEmployee(self.first_name3, self.last_name3, self.role3, self.amount3)

        def test_init(self):
            self.assertEqual((self.emploee1.first_name, self.emploee1.last_name, self.emploee1.role, self.emploee1.vacation_days), (str(self.first_name1), str(self.last_name1),str(self.role1), int(self.vacation_days)))
            self.assertEqual((self.emploee2.first_name, self.emploee2.last_name, self.emploee2.role,self.emploee2.vacation_days, self.emploee2.salary),
                             (str(self.first_name2), str(self.last_name2), str(self.role2), int(self.vacation_days), int(self.salary)))
            self.assertEqual((self.emploee3.first_name, self.emploee3.last_name, self.emploee3.role, self.emploee3.amount, self.emploee1.vacation_days),
                             (str(self.first_name3), str(self.last_name3), str(self.role3), 0, int(self.vacation_days)))


        def test_full_name(self):
            self.assertEqual(self.emploee1.fullname, self.first_name1 + ' ' + self.last_name1)
            self.assertEqual(self.emploee2.fullname, self.first_name2 + ' ' + self.last_name2)
            self.assertEqual(self.emploee3.fullname, self.first_name3 + ' ' + self.last_name3)

        def test__str__(self):
            self.assertEqual(self.emploee1.fullname, 'Ihor Kozakov')
            self.assertEqual(self.emploee2.fullname, 'Georg Kirichenko')
            self.assertEqual(self.emploee3.fullname, 'Olha Okpenko')

        def test_log_work(self):
            self.assertEqual(self.emploee1.amount, 0)
            self.assertEqual(self.emploee3.amount, 0)

        def test_obj_instance(self):
            self.assertIsInstance(self.emploee1, HourlyEmployee)
            self.assertIsInstance(self.emploee2, SalariedEmployee)
            self.assertIsInstance(self.emploee3, HourlyEmployee)

        def test_take_holiday(self):
            self.assertEqual(self.emploee2.take_holiday(True), None)
            self.assertEqual(self.emploee1.take_holiday(False), None)





if __name__ == '__main__':
    unittest.main()