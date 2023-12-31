# Generated by Django 4.2.4 on 2023-08-07 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_buy_options_prod_buy_options_color_prod_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='payment_options',
            field=models.CharField(choices=[('cash', 'cash'), ('credit_card', 'credit_card')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prod',
            name='price',
            field=models.IntegerField(default=500),
        ),
    ]
