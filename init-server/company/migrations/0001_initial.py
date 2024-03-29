# Generated by Django 5.0.1 on 2024-01-09 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                ("type", models.CharField(blank=True, max_length=100, null=True)),
                ("about", models.TextField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "company_logo",
                    models.ImageField(blank=True, null=True, upload_to="company_logo/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HunterProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="hunter_profile/"
                    ),
                ),
                ("designation", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.companyprofile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("position", models.CharField(blank=True, max_length=100, null=True)),
                ("hard_skill", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("vacancy", models.PositiveIntegerField(default=1)),
                ("experience", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                ("salary", models.IntegerField(default=0.0)),
                ("publish_date", models.DateField(auto_now_add=True)),
                ("close_date", models.DateField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.companyprofile",
                    ),
                ),
                (
                    "hunter",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.hunterprofile",
                    ),
                ),
            ],
        ),
    ]
