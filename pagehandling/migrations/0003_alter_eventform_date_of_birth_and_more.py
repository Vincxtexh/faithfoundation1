# Generated by Django 4.1.4 on 2023-01-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagehandling', '0002_eventform_city_eventform_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventform',
            name='date_of_birth',
            field=models.CharField(default='02/12/1990', max_length=8),
        ),
        migrations.AlterField(
            model_name='eventform',
            name='postal_code',
            field=models.IntegerField(default='411001'),
        ),
    ]
