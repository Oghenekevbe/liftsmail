# Generated by Django 4.2.13 on 2024-07-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_rename_group_contact_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]