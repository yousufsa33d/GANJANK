# Generated by Django 3.0.7 on 2020-06-22 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200623_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
