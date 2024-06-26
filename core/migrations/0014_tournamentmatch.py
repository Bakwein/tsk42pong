# Generated by Django 5.0.3 on 2024-04-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_tournament_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentMatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament', models.CharField(max_length=100)),
                ('player1', models.CharField(max_length=100)),
                ('player2', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
