from faker import Faker
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')
django.setup()

import random
from my_app.models import Topic, WebPage, AccessRecord

fakegen = Faker()

topic_names = ['Strategy', 'Finance', 'Politics', 'Technology', 'Dogs']


def populate(n_records: int):
    for index in range(n_records):
        topic = Topic.objects.get_or_create(topic_name=random.choice(topic_names))[0]
        topic.save()
        url = fakegen.url()
        date = fakegen.date()
        name = fakegen.company()

        webpage = WebPage.objects.get_or_create(topic=topic, name=name, url=url)[0]
        webpage.save()

        access_record = AccessRecord.objects.get_or_create(webpage=webpage, date=date)[0]
        access_record.save()


if __name__ == '__main__':
    n_records = 20
    print('Populating {} records..'.format(n_records))
    populate(n_records=n_records)
    print('Done')
