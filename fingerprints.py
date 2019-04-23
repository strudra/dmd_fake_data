import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 200000
fake = Faker()


def create_csv_file():
    with open('./files/fingerprints.csv', 'w', newline='') as csvfile:
        fieldnames = ['fingerprint_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'fingerprint_code': fake.sha256(raw_output=False)
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
