# Generated by Django 4.2.16 on 2024-12-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
    ]
