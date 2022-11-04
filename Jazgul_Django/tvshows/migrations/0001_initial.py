# Generated by Django 4.1 on 2022-11-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('DETECTIVE', 'DETECTIVE'), ('HORROR', 'HORROR'), ('ANIME', 'ANIME'), ('MELODRAMA', 'MELODRAMA'), ('FAIRYTAILES', 'FAIRYTAIL')], max_length=100)),
                ('quantity', models.IntegerField()),
                ('trailer', models.URLField()),
            ],
        ),
    ]