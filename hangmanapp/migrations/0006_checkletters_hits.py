# Generated by Django 4.0.5 on 2022-09-06 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangmanapp', '0005_checkletters_fails'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkletters',
            name='hits',
            field=models.SmallIntegerField(default=0),
        ),
    ]