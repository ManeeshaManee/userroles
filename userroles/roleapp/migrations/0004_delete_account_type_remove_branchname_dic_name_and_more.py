# Generated by Django 4.1.5 on 2023-08-23 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roleapp', '0003_delete_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account_type',
        ),
        migrations.RemoveField(
            model_name='branchname',
            name='dic_name',
        ),
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Branchname',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
