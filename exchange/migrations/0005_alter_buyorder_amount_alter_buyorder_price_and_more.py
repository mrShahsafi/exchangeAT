# Generated by Django 4.2.11 on 2024-03-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0004_alter_exchange_content_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyorder",
            name="amount",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="buyorder",
            name="price",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="sellorder",
            name="amount",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="sellorder",
            name="price",
            field=models.FloatField(default=0),
        ),
    ]