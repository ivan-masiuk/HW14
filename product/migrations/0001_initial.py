# Generated by Django 3.1.5 on 2021-01-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Noname product', max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
