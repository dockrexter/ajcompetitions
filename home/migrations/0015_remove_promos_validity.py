# Generated by Django 3.2.3 on 2021-06-09 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_promos_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promos',
            name='validity',
        ),
    ]
