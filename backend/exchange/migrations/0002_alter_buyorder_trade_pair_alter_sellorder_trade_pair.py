# Generated by Django 4.2.11 on 2024-03-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyorder",
            name="trade_pair",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="exchange.tradingpair",
            ),
        ),
        migrations.AlterField(
            model_name="sellorder",
            name="trade_pair",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="exchange.tradingpair",
            ),
        ),
    ]
