# Generated by Django 3.0.1 on 2020-04-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('job_name', models.TextField(max_length=50)),
                ('job_text', models.TextField(max_length=255)),
            ],
        ),
    ]
