# Generated by Django 4.2.3 on 2023-08-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_invoice_line_one_unit_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='line_one_unit_price',
        ),
        migrations.AddField(
            model_name='invoice',
            name='line_one_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
    ]
