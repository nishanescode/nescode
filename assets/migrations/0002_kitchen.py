# Generated by Django 2.0.9 on 2018-11-21 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingrediants', models.TextField()),
                ('manufactured_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
