# Generated by Django 4.2.3 on 2023-07-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samdjangoproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=40)),
                ('tscnumber', models.CharField(max_length=50)),
            ],
        ),
    ]