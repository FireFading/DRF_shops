# Generated by Django 4.2 on 2023-04-19 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("towns", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Street",
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
                ("name", models.CharField(max_length=128, verbose_name="Название")),
                (
                    "town",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shops",
                        to="towns.town",
                        verbose_name="Город",
                    ),
                ),
            ],
            options={
                "verbose_name": "Улица",
                "verbose_name_plural": "Улицы",
                "ordering": ["-name"],
            },
        ),
    ]
