# Generated by Django 3.2.4 on 2021-06-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('channel_id', models.CharField(max_length=255)),
                ('channel_name', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=255)),
            ],
        ),
    ]
