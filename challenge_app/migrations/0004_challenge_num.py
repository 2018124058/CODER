# Generated by Django 4.0.6 on 2022-07-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_app', '0003_challenge_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
