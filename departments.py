import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 1000
fake = Faker()


def create_csv_file():
    with open('./files/departments.csv', 'w', newline='') as csvfile:
        fieldnames = ['department_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'department_name': fake.company()
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
