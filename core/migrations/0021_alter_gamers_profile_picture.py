# Generated by Django 5.0.3 on 2024-04-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_gamers_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamers',
            name='profile_picture',
            field=models.TextField(),
        ),
    ]
