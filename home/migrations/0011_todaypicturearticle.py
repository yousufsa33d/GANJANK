# Generated by Django 3.0.7 on 2020-07-05 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_article_publish'),
        ('home', '0010_today'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayPictureArticle',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.HomepageDate')),
            ],
        ),
    ]
