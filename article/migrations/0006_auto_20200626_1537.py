# Generated by Django 3.0.7 on 2020-06-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200626_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleheading',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='article/images'),
        ),
    ]
