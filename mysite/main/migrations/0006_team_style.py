# Generated by Django 3.2.12 on 2022-03-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='style',
            field=models.TextField(default=''),
        ),
    ]