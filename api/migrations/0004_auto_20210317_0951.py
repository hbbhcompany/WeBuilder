# Generated by Django 3.1.6 on 2021-03-17 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210317_0939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cards',
            new_name='Card',
        ),
    ]
