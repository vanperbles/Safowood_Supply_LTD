# Generated by Django 2.2.13 on 2020-07-15 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_item_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]
