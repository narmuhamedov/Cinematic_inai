# Generated by Django 4.1 on 2022-11-16 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentTvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='tvshow.tvshow')),
            ],
        ),
    ]
