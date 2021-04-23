# Generated by Django 3.0.8 on 2021-04-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20210423_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='exchange',
            name='cryptos',
            field=models.ManyToManyField(related_name='cryptos', to='card.Crypto'),
        ),
        migrations.AddField(
            model_name='exchange',
            name='currencies',
            field=models.ManyToManyField(related_name='currencies', to='card.Currency'),
        ),
    ]
