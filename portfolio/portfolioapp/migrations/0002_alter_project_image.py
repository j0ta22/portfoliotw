# Generated by Django 4.2.3 on 2023-07-09 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolioapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="portfolio/images/"),
        ),
    ]
