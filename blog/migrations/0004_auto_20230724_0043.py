# Generated by Django 3.2.20 on 2023-07-23 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]