# Generated by Django 3.2.9 on 2022-02-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dar', '0008_auto_20220120_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]