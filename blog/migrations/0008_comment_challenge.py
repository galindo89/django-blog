# Generated by Django 4.2.16 on 2024-12-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_field_2_remove_post_field_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='Comment'),
        ),
    ]
