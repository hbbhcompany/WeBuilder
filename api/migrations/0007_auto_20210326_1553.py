# Generated by Django 3.1.6 on 2021-03-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210318_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='adminName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='orderAccepted',
            field=models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('NotAccepted', 'NotAccepted')], default='NotAccepted', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='timeArrive',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='workerName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
