# Generated by Django 5.0.1 on 2024-01-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidate", "0004_candidateprofile_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidateprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]