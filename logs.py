import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 100000
fake = Faker()


def create_csv_file():
    with open('./files/logs.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'event', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'date': fake.unix_time(end_datetime=None, start_datetime=None),
                    'event': fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
                    'message': fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
