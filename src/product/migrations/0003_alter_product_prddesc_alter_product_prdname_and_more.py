# Generated by Django 4.2.3 on 2023-07-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_prddesc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="prdDesc",
            field=models.TextField(verbose_name="Product Description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="prdName",
            field=models.CharField(max_length=100, verbose_name="Product Name"),
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("proIMage", models.ImageField(upload_to="product/")),
                (
                    "proProduct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                        verbose_name="Product",
                    ),
                ),
            ],
        ),
    ]
