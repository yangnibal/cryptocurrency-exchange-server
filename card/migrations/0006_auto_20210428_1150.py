# Generated by Django 3.2 on 2021-04-28 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_auto_20210427_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='nameEN',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='crypto',
            name='nameKR',
        ),
    ]