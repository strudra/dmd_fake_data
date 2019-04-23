import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 10000
fake = Faker()


def create_csv_file():
    with open('./files/employees.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name()
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
