# Generated by Django 5.1.7 on 2025-03-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
