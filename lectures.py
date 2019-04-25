import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 100000
fake = Faker()


def create_csv_file():
    with open('./files/lectures.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'date': fake.unix_time(end_datetime=None, start_datetime=None),
                    'duration': fake.word(ext_word_list=['60', '90', '45', '120', '180'])
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
