from faker import Faker

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')
django.setup()
from my_app.models import User

fakegen = Faker()


def populate(n_records: int):
    for index in range(n_records):
        name = fakegen.name().split()
        first_name = name[0]
        last_name = name[-1]
        email = fakegen.email()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        user.save()


if __name__ == '__main__':
    populate(20)
