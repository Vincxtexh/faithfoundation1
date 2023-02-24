# Generated by Django 4.1.4 on 2023-02-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagehandling', '0008_smallevent_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Event Title')),
                ('description', models.TextField(max_length=300, verbose_name='Description')),
                ('banner_image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('subject', models.CharField(max_length=70, verbose_name='Subject')),
                ('mobile_number', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Mobile Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('venue', models.CharField(max_length=150)),
                ('manager', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=900)),
                ('event_image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='LandingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Event Name')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(max_length=70, verbose_name='Description')),
                ('notification', models.CharField(max_length=10, verbose_name='Notification')),
                ('banner_image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='smallEvent',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='city',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='date_submitted',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='mother_tongue',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='permenant_address',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='eventform',
            name='state',
        ),
        migrations.AddField(
            model_name='eventform',
            name='count_of_family',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='eventform',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventform',
            name='first_name',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='eventform',
            name='last_name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
