# Generated by Django 4.1.4 on 2023-01-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="jon",
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
                ("company", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "descriptions",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
