# Generated by Django 3.2.12 on 2022-03-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220311_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coef', models.IntegerField(default=100)),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='step_1_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='step_2_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='step_3_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='step_4_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='step_5_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='step_6_score',
            field=models.IntegerField(default=0),
        ),
    ]