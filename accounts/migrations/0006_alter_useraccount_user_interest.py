# Generated by Django 4.2 on 2023-04-07 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_interest_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user_interest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.interest'),
            preserve_default=False,
        ),
    ]
