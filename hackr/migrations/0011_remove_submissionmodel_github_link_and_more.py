# Generated by Django 4.2 on 2023-05-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hackr", "0010_alter_hackathonsmodel_enddatetime_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submissionmodel",
            name="github_link",
        ),
        migrations.RemoveField(
            model_name="submissionmodel",
            name="submisiion_file",
        ),
        migrations.AddField(
            model_name="submissionmodel",
            name="submission_file",
            field=models.FileField(blank=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="submissionmodel",
            name="submission_link",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
