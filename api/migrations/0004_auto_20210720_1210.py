# Generated by Django 3.0 on 2021-07-20 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_gamelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelog',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamelogs', to='api.Player'),
        ),
    ]
