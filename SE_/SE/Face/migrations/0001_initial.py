# Generated by Django 3.2.7 on 2021-09-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=9)),
                ('<django.db.models.fields.CharField>_<django.db.models.fields.CharField>', models.ImageField(default='default.jpg', upload_to='imgofstud/')),
            ],
        ),
    ]
