# Generated by Django 4.2.3 on 2023-07-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samdjangoproject', '0005_alter_people_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='city',
            field=models.CharField(default=254, max_length=30),
        ),
        migrations.AddField(
            model_name='people',
            name='country',
            field=models.CharField(default=254, max_length=30),
        ),
    ]