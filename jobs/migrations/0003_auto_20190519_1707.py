# Generated by Django 2.2.1 on 2019-05-19 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190519_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]
