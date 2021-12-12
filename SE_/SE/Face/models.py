from django.db import models
import os
from uuid import uuid4
# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'imgofstud'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format("{}_{}".format(instance.name,instance.roll), "jpeg")
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class student(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=9)
    image=models.ImageField(default='default.jpg',upload_to=path_and_rename,blank=True,null=True)
