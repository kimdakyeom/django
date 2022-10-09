# Generated by Django 3.2.13 on 2022-10-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.CharField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], max_length=10),
        ),
    ]
