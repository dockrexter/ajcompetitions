# Generated by Django 3.2 on 2021-05-16 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210512_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='ticket_price',
            new_name='price',
        ),
    ]
