# Generated by Django 3.0.7 on 2020-07-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200705_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doyouknow',
            old_name='DoYouKnow',
            new_name='doYouKnow',
        ),
    ]