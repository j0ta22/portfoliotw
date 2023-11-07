# Generated by Django 4.2.3 on 2023-07-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="portafolio/images/")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
