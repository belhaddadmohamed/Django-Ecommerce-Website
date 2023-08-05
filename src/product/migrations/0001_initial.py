# Generated by Django 4.2.3 on 2023-07-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("prdName", models.CharField(max_length=100)),
                ("prdDesc", models.TextField(max_length=100)),
                ("prdPrice", models.DecimalField(decimal_places=2, max_digits=5)),
                ("prdCost", models.DecimalField(decimal_places=2, max_digits=5)),
                ("prdCreated", models.DateTimeField()),
            ],
        ),
    ]