# Generated by Django 3.2.13 on 2022-11-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sendgrid", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="email",
            name="payload",
            field=models.JSONField(),
        ),
    ]
