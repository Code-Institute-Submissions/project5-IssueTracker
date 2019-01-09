# Generated by Django 2.0.9 on 2019-01-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20190108_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuemodel',
            name='type',
            field=models.CharField(choices=[('FEATURE', 'Feature'), ('BUG', 'Bug')], default='BUG', max_length=7),
        ),
    ]