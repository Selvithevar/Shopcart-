# Generated by Django 4.2.1 on 2023-06-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_favourite"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favourite",
            old_name="Product",
            new_name="product",
        ),
    ]
