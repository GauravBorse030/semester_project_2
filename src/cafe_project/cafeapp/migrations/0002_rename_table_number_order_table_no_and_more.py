# Generated by Django 5.1.4 on 2025-04-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='table_number',
            new_name='table_no',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(),
        ),
    ]
