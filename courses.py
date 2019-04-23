import csv
import random
from time import time
from decimal import Decimal
from faker import Faker

RECORD_COUNT = 76
fake = Faker()

courses = [
    'DataBases 2',
    'Accounting & Finance',
    'Aeronautical & Manufacturing Engineering',
    'Agriculture & Forestry',
    'American Studies',
    'Anatomy & Physiology',
    'Anthropology',
    'Archaeology',
    'Architecture',
    'Art & Design',
    'Aural & Oral Sciences',
    'Biological Sciences',
    'Building',
    'Business & Management Studies',
    'Celtic Studies',
    'Chemical Engineering',
    'Chemistry',
    'Civil Engineering',
    'Classics & Ancient History',
    'Communication & Media Studies',
    'Complementary Medicine',
    'Computer Science',
    'Counselling',
    'Creative Writing',
    'Criminology',
    'Dentistry',
    'Drama, Dance & Cinematics',
    'East & South Asian Studies',
    'Economics',
    'Education',
    'Electrical & Electronic Engineering',
    'English',
    'Fashion'
    'Film Making',
    'Food Science',
    'Forensic Science',
    'French',
    'Geography & Environmental Sciences',
    'Geology',
    'General Engineering',
    'German',
    'History',
    'History of Art, Architecture & Design',
    'Hospitality, Leisure, Recreation & Tourism',
    'Iberian Languages/Hispanic Studies',
    'Italian',
    'Land & Property Management',
    'Law',
    'Librarianship & Information Management',
    'Linguistics',
    'Marketing',
    'Materials Technology',
    'Mathematics',
    'Mechanical Engineering',
    'Medical Technology',
    'Medicine',
    'Middle Eastern & African Studies',
    'Music',
    'Nursing',
    'Occupational Therapy',
    'Optometry, Ophthalmology & Orthoptics',
    'Pharmacology & Pharmacy',
    'Philosophy',
    'Physics and Astronomy',
    'Physiotherapy',
    'Politics',
    'Psychology',
    'Robotics',
    'Russian & East European Languages',
    'Social Policy',
    'Social Work',
    'Sociology',
    'Sports Science',
    'Theology & Religious Studies',
    'Town & Country Planning and Landscape Design',
    'Veterinary Medicine',
    'Youth Work'
]


def create_csv_file():
    with open('./files/courses.csv', 'w', newline='') as csvfile:
        fieldnames = ['course_name', 'course_description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'course_name': courses[i],
                    'course_description': fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
                }
            )


if __name__ == '__main__':
    start = time()
    create_csv_file()
    # print(len(courses))
