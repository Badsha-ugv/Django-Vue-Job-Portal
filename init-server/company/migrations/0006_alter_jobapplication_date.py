# Generated by Django 5.0.1 on 2024-01-15 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0005_alter_companyprofile_user_alter_jobapplication_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="date",
            field=models.DateField(
                verbose_name=datetime.datetime(2024, 1, 15, 21, 40, 20, 660646)
            ),
        ),
    ]
