import datetime as dt
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(f'Приветствую Вас, текущая дата и время: {dt.datetime.now()}')
    calculate_salary()
    get_employees()






