# Generated by Django 4.1.1 on 2022-12-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_date_joined_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]