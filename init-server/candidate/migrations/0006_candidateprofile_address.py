# Generated by Django 5.0.1 on 2024-01-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidate", "0005_candidateprofile_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidateprofile",
            name="address",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
