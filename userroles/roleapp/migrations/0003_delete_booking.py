# Generated by Django 4.1.5 on 2023-08-23 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roleapp', '0002_remove_person_ac_type_remove_person_branch_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]