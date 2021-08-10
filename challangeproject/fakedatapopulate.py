import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","challangeproject.settings")

import django

django.setup()



import random
from challangeapp.models import  AccessRecord,Webpage,Topic,User
from faker import Faker

from random import seed
from random import random
from random import randint

seed(1)

fakegen = Faker()
#
# topics = ['Search','Social','Markertplace','News','Games']
#
#
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
#
# def populate(N=5):
#     for entry in range(N):
#         top = add_topic()
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         webpg = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]
#         webpg.save()
#         acc_rec = AccessRecord.objects.get_or_create(name = webpg,date=fake_date)[0]
#         acc_rec.save()

def populate_User(N=5):
    for entry in range(N):
        # top = add_topic()
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        # fake_name = fakegen.company()
        #
        # webpg = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]
        # webpg.save()
        # acc_rec = AccessRecord.objects.get_or_create(name = webpg,date=fake_date)[0]
        # acc_rec.save()
        name1 = fakegen.name()
        age1 = randint(0, 100)
        print(name1)
        print(age1)
        user = User.objects.get_or_create(name = name1, age=age1)[0]
        user.save()

if __name__ == '__main__':
    print("populating db")
    populate_User(20)
    print("populating complete")
