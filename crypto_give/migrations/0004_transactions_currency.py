# Generated by Django 4.1.6 on 2023-07-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_give', '0003_remove_time_status_alter_time_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='currency',
            field=models.CharField(default='BTC', max_length=50, verbose_name='Currency'),
        ),
    ]