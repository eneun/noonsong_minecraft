# Generated by Django 3.0.7 on 2020-09-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0003_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]