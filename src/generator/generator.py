import random

from src.data.data_user import User
from faker import Faker

faker_en = Faker('En')


def generator_user():
    return User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email()
    )


def generator_file():
    path_file = rf"D:\python_selenium\test{random.randint(1, 10)}.txt"
    file = open(path_file, 'w')
    file.write(f'Hello{random.randint(1, 10)}')
    file.close()
    return path_file
