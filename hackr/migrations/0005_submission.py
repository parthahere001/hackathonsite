# Generated by Django 4.2 on 2023-05-01 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hackr", "0004_hackathonsmodel_tagline_alter_hackathonsmodel_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="submission",
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
                ("name", models.CharField(max_length=200)),
                ("summary", models.CharField(max_length=500)),
                ("submission_link", models.CharField(max_length=1000)),
                ("submisiion_file", models.FileField(upload_to="")),
                (
                    "hkr",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hackr.hackersmodel",
                    ),
                ),
                (
                    "hkthn",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hackr.hackathonsmodel",
                    ),
                ),
            ],
        ),
    ]
