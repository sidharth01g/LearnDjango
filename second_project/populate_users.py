from faker import Faker
from my_app.models import User
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')
django.setup()

fakegen = Faker()


def populate(n_records: int):
    for index in range(n_records):
        first_name = fakegen.name()
        last_name = fakegen.name()
        email = fakegen.email()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        user.save()


if __name__ == '__main__':
    populate(20)
