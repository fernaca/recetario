# Generated by Django 4.0.1 on 2022-01-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_on_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='test', max_length=200, unique=True),
        ),
    ]
