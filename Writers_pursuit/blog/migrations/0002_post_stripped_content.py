# Generated by Django 4.1.3 on 2023-04-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stripped_content',
            field=models.TextField(default='.'),
        ),
    ]
