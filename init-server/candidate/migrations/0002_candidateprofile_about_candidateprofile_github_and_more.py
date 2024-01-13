# Generated by Django 5.0.1 on 2024-01-10 06:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidate", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="candidateprofile",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="github",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="hard_skill",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="linkedin",
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="profile_avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="candidate_profile/"
            ),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to="resume/"),
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="slug",
            field=models.SlugField(default="", unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Award",
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
                ("topic", models.CharField(max_length=150)),
                ("title", models.CharField(max_length=200)),
                ("organization", models.CharField(max_length=150)),
                ("date", models.DateField(blank=True, null=True)),
                ("link", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="awards",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="award",
            field=models.ManyToManyField(blank=True, to="candidate.award"),
        ),
        migrations.CreateModel(
            name="Education",
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
                ("exam", models.CharField(max_length=100)),
                ("institute", models.CharField(max_length=200)),
                ("passing_year", models.CharField(max_length=50)),
                ("result", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="education",
            field=models.ManyToManyField(blank=True, to="candidate.education"),
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("title", models.CharField(max_length=200)),
                ("company", models.CharField(blank=True, max_length=150, null=True)),
                ("location", models.CharField(blank=True, max_length=80, null=True)),
                ("duration", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="candidateprofile",
            name="experience",
            field=models.ManyToManyField(
                blank=True, null=True, to="candidate.experience"
            ),
        ),
    ]