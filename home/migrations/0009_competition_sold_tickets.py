# Generated by Django 3.2 on 2021-05-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_ticket_price_competition_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='sold_tickets',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
