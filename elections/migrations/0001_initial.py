# Generated by Django 2.1.7 on 2019-05-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MMIM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=10)),
                ('user_pw', models.CharField(max_length=10)),
                ('adr1', models.CharField(max_length=10)),
                ('pn', models.CharField(max_length=10)),
                ('jm', models.CharField(max_length=10)),
                ('choice', models.CharField(max_length=10)),
            ],
        ),
    ]
