# Generated by Django 4.2.16 on 2024-12-08 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=1),
        ),
    ]