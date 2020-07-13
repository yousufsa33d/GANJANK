# Generated by Django 3.0.7 on 2020-07-01 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0012_articleedit_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('post', models.TextField()),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_title1', models.CharField(blank=True, max_length=200, null=True)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_title2', models.CharField(blank=True, max_length=200, null=True)),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_title3', models.CharField(blank=True, max_length=200, null=True)),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_title4', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
