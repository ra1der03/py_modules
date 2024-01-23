from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from stringcolor import *

if __name__ == '__main__':
    print(cs(datetime.today(), "DeepPink3"))
    calculate_salary(cs('33333',"orchid"))
    get_employees(cs('ryan', "yellow"))