import os
os.environ.setdefault('DJANGO_SETTINGS_MIDULE','First_one.settings')

import django
django.setup()

# fake pop script
import random
from First_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def population(N=5):

    # get the topic for the entry
    for entry in range(N):
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        # Create th new webpage entry
        webpg = webpage.object.get_or_create(topic=top,url=fake,name=fake_name)[0]

        # Create a fake AccessRecord for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

    if __name__ == '__main__':
        print("populating Script!")
        populate(20)
        print("populating Complete!")
