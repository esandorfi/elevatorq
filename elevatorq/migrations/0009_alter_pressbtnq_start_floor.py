# Generated by Django 3.2.3 on 2021-05-21 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevatorq', '0008_auto_20210521_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressbtnq',
            name='start_floor',
            field=models.SmallIntegerField(help_text='floor between min 0 and max 47 depends on your direction', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(47)]),
        ),
    ]
