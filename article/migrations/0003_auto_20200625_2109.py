# Generated by Django 3.0.7 on 2020-06-25 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200625_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleheading',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.ArticleHeading'),
        ),
    ]
