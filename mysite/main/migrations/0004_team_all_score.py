# Generated by Django 3.2.12 on 2022-03-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220313_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='all_score',
            field=models.IntegerField(default=0),
        ),
    ]