# Generated by Django 5.0.6 on 2024-05-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(max_length=50, unique=True)),
                ('img', models.FileField(upload_to='language')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
