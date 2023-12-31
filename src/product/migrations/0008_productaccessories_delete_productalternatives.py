# Generated by Django 4.2.3 on 2023-07-29 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_alter_category_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductAccessories",
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
                (
                    "accAccessories",
                    models.ManyToManyField(
                        related_name="Product_accessories", to="product.product"
                    ),
                ),
                (
                    "accProduct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="main_product",
                        to="product.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Accessory",
                "verbose_name_plural": "Product Accessories",
            },
        ),
        migrations.DeleteModel(
            name="ProductAlternatives",
        ),
    ]
