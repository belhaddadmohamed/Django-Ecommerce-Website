# Generated by Django 4.2.3 on 2023-08-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0013_remove_product_prdvariant"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="prdImage",
            field=models.ImageField(blank=True, null=True, upload_to="product/"),
        ),
    ]
