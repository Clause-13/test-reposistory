import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
django.setup()

## Fake population 

import random
from appTwo.models import User,AccessRecord,Webpage,Topic  
from faker import Faker

fakegen = Faker()

def add_topic():
    t = Topic.objects.get_or_create(top_name='Users')[0]
    t.save
    return t

def populate_user(N=5):
    for entry in range(N):

        #get topic for entry:
        top = add_topic()

        #create fake url:
        fake_url = fakegen.url()

        #create fake users:
        fake_f_name = fakegen.first_name()
        fake_l_name = fakegen.last_name()
        fake_email = fakegen.email()

        #create webpage new entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_email)[0]

        #create users new entry:
        usrs = User.objects.get_or_create(first_name=fake_f_name,last_name=fake_l_name,email_addr=fake_email)[0]


if __name__ == "__main__":
    print("populating scripts")
    populate_user(5)
    print("populatating complete!")        
