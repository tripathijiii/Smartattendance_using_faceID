# Generated by Django 3.2.7 on 2021-09-16 08:28

import Face.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face', '0003_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=Face.models.path_and_rename),
        ),
    ]
