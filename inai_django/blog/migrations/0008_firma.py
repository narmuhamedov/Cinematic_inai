# Generated by Django 4.1 on 2022-11-08 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_text_about_us_textssssssss'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('total_cost', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
