"""
A very advanced employee management system

"""

import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyTypeChecker
@dataclass
class Employee:
    """Basic employee representation"""

    first_name: str
    last_name: str
    role: str
    vacation_days: int = 25

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.fullname

    def take_holiday(self, payout: bool = False) -> None:
        """Take a single holiday or a payout vacation"""

        if payout:
            try:
                if self.vacation_days < 5:
                    msg = f"{self} have not enough vacation days. " \
                          f"Remaining days: %d. Requested: %d" % (self.vacation_days, 5)
                    raise ValueError(msg)
                self.vacation_days -= 5
                msg = f"{self} taking a holiday. Remaining vacation days: %d" % self.vacation_days
                logger.info(msg)
            except ValueError as er:
                logger.info(er)
        else:
            try:
                if self.vacation_days < 1:
                    remaining = self.vacation_days
                    msg = f"{self} have not enough vacation days. " \
                          f"Remaining days: %d. Requested: %d" % (self.vacation_days, 1)
                    raise ValueError(msg)
                self.vacation_days -= 1
                msg = f"{self} taking a payout. Remaining vacation days: %d" % self.vacation_days
                logger.info(msg)
            except ValueError as er:
                logger.info(er)


# noinspection PyTypeChecker
@dataclass
class HourlyEmployee(Employee):
    """Represents employees who are paid on worked hours base"""

    amount: int = 0
    hourly_rate: int = 50

    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.amount += hours


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: int = 5000


# noinspection PyTypeChecker
class Company:
    """A company representation"""

    def __init__(self, title: str, employees: list = []):
        self.title = title
        self.employees = employees

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Company (title = {self.title}, employees = {self.employees})'

    def add_to_company(self, employee: Employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        if isinstance(employee, list):
            self.employees += employee

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role == "CEO":
                result.append(employee.fullname)
        return result

    def get_managers(self) -> list[Employee]:
        """Return employees list with role of manager"""

        result = []
        for employee in self.employees:
            if employee.role == "manager":
                result.append(employee.fullname)
        return result

    def get_developers(self) -> list[Employee]:
        """Return employees list with role of developer"""

        result = []
        for employee in self.employees:
            if employee.role == "dev":
                result.append(employee.fullname)
        return result

    @staticmethod
    def pay(employee: Employee) -> None:
        """Pay to employee"""

        if isinstance(employee, SalariedEmployee):
            msg = (
                "Paying monthly salary of %.2f to %s"
            ) % (employee.salary, employee)
            logger.info(msg)

        if isinstance(employee, HourlyEmployee):
            msg = (
                "Paying %s hourly rate of %.2f for %d hours. Total: %.2f"
            ) % (employee, employee.hourly_rate, employee.amount, employee.hourly_rate*employee.amount)
            logger.info(msg)

    def pay_all(self, employees: list) -> None:
        """Pay all the employees in this company"""
        
        for employee in employees:
            self.pay(employee)

        # TODO: implement this method


def main():
    employee_1 = HourlyEmployee(first_name="Ihor", last_name="Kozakov", role="CEO", amount=20)
    employee_2 = SalariedEmployee(first_name="Georg", last_name="Kirichenko", role="manager")
    employee_3 = HourlyEmployee(first_name="Olha", last_name="Okpenko", role="dev", amount=60)
    employees = [employee_1, employee_2, employee_3]
    company = Company(title='google', employees=employees)
    company.pay_all(employees)


if __name__ == "__main__":
    main()
