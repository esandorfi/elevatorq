# Generated by Django 3.2.3 on 2021-05-21 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elevatorq', '0002_auto_20210521_1019'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Elevator',
            new_name='BuildingElevator',
        ),
        migrations.AlterModelOptions(
            name='buildingelevator',
            options={'ordering': ['name'], 'verbose_name': 'Building Elevators', 'verbose_name_plural': 'Building Elevators'},
        ),
        migrations.AlterModelOptions(
            name='elevatorq',
            options={'ordering': ['create_time'], 'verbose_name': 'Elevator Q', 'verbose_name_plural': 'Elevator Q'},
        ),
        migrations.AlterModelOptions(
            name='pressbtnq',
            options={'ordering': ['create_time'], 'verbose_name': 'Press Button Q', 'verbose_name_plural': 'Press Button Q'},
        ),
    ]
