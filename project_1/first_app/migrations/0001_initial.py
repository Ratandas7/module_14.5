# Generated by Django 5.1 on 2024-09-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
