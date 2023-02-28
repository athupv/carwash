# Generated by Django 4.1 on 2022-11-24 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customer.users'),
            preserve_default=False,
        ),
    ]
