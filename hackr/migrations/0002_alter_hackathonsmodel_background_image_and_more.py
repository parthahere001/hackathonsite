# Generated by Django 4.1 on 2023-04-28 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hackr", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackathonsmodel",
            name="background_image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="hackathonsmodel",
            name="hackathon_image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
