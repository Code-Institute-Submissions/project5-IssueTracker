# Generated by Django 2.0.9 on 2019-01-30 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]
