# Generated by Django 4.2 on 2023-05-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hackr", "0009_remove_hackathonsmodel_background_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackathonsmodel",
            name="enddatetime",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="hackathonsmodel",
            name="startdatetime",
            field=models.DateField(),
        ),
    ]