# Generated by Django 4.1 on 2022-08-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba', '0005_alter_player_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.AddField(
            model_name='player',
            name='pos',
            field=models.CharField(default='pos', max_length=100),
        ),
    ]
