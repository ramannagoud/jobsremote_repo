import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','moviesproject1.settings')
import django
django.setup()

from testapp.models import Jobs
from random import *
from faker import Faker
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project Manager','TL','clark','se','jr.asst'))
        feligibility=fake.random_element(elements=('MCA','BTECT','MSC','SSC'))
        faddress=fake.address()
        femail=fake.email()
        fphoneno=phonenumbergen()
        jobs_record=Jobs.objects.get_or_create(date=fdate,companyname=fcompany,title=ftitle,eligibility=feligibility,
        address=faddress,email=femail,phoneno=fphoneno)
populate(30)
