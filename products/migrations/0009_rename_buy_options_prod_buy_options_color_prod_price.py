# Generated by Django 4.2.4 on 2023-08-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_prod_buy_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prod',
            old_name='buy_options',
            new_name='buy_options_color',
        ),
        migrations.AddField(
            model_name='prod',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]