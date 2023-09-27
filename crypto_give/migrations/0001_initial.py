# Generated by Django 4.1.6 on 2023-07-25 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(default=247, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Days')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='Pending', max_length=50, verbose_name='Wallet Address')),
                ('deposit', models.CharField(default='Pending', max_length=50, verbose_name='Deposit')),
                ('received', models.CharField(default='Pending', max_length=50, verbose_name='Received')),
                ('status', models.CharField(default='Success', max_length=50, verbose_name='Status')),
            ],
        ),
    ]