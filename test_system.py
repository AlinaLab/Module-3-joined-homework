def main():
    employee_1 = HourlyEmployee(first_name="Ihor", last_name="Kozakov", role="CEO", amount=20)
    employee_2 = SalariedEmployee(first_name="Georg", last_name="Kirichenko", role="manager")
    employee_3 = HourlyEmployee(first_name="Olha", last_name="Okpenko", role="dev", amount=60)
    employees = [employee_1, employee_2, employee_3]
    company = Company(title='google', employees=employees)
    company.pay_all(employees)


if __name__ == "__main__":
    main()