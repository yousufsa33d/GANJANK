# Generated by Django 3.0.7 on 2020-06-28 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0009_articlefeedback_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleEdit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('old', models.TextField()),
                ('changes', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]