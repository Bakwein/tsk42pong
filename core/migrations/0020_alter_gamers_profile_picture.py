# Generated by Django 5.0.3 on 2024-04-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_gamers_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamers',
            name='profile_picture',
            field=models.CharField(max_length=15800),
        ),
    ]
