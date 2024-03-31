# Generated by Django 4.2.6 on 2023-11-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('point', models.IntegerField()),
            ],
        ),
    ]
