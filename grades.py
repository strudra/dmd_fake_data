import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 100000
fake = Faker()


def create_csv_file():
    with open('./files/grades.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'date': fake.unix_time(end_datetime=None, start_datetime=None),
                    'value': fake.word(ext_word_list=['A', 'B', 'C', 'D', 'F'])
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
