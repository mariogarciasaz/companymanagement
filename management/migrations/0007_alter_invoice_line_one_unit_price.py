# Generated by Django 4.2.3 on 2023-08-07 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_alter_invoice_line_one_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_one_unit_price',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.product', to_field='price'),
        ),
    ]
