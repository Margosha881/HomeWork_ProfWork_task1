import datetime as dt
from application import salary
from application.db import people

if __name__ == '__main__':
    print(f'Приветствую Вас, текущая дата и время: {dt.datetime.now()}')
    salary.calculate_salary()
    people.get_employees()

