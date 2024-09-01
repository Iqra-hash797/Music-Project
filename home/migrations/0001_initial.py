# Generated by Django 5.1 on 2024-08-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('singer', models.CharField(max_length=2000)),
                ('tags', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images')),
                ('song', models.FileField(upload_to='images')),
                ('movie', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
