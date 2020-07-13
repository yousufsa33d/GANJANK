# Generated by Django 3.0.7 on 2020-06-25 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]