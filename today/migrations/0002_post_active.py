# Generated by Django 3.0.1 on 2020-11-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
