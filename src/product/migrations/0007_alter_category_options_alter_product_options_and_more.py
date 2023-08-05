# Generated by Django 4.2.3 on 2023-07-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_alter_category_catparent"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "verbose_name": "Product image",
                "verbose_name_plural": "Product images",
            },
        ),
        migrations.CreateModel(
            name="ProductAlternatives",
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
                    "prdAl_Alternatives",
                    models.ManyToManyField(
                        related_name="Product_Alternatives", to="product.product"
                    ),
                ),
                (
                    "prdAl_Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Product_name",
                        to="product.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Alternative",
                "verbose_name_plural": "Alternatives",
            },
        ),
    ]
