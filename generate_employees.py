import random
import names
from faker import Faker
from datetime import date

with open('./additional_employees_1.sql', 'w') as f:  # additional_employees_2.sql
    fake = Faker()
    start_index = 50000  # 50000 = 50000 ~ 74999 | 75000 = 75000 ~ 99999

    for i in range(start_index, start_index + 25000):
        gender_key = random.choice(['male', 'female'])
        emp_no = i
        birth_date = fake.date_between(
            start_date=date(year=1970, month=1, day=1),
            end_date=date(year=1989, month=12, day=31)
        )
        first_name = names.get_first_name(gender=gender_key)
        last_name = names.get_last_name()
        gender = gender_key[0].upper()
        hire_date = fake.date_between(
            start_date=date(year=1990, month=1, day=1),
            end_date=date(year=2009, month=12, day=31)
        )

        sql = """INSERT INTO employees VALUES ('{}', '{}', '{}', '{}', '{}', '{}');\n""".format(
            emp_no, birth_date, first_name, last_name, gender, hire_date
        )
        f.write(sql)
