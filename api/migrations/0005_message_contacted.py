# Generated by Django 3.1.6 on 2021-03-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210317_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='contacted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
