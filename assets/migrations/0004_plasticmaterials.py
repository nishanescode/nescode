# Generated by Django 2.0.9 on 2018-11-21 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_furnitures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plasticmaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quality', models.TextField()),
                ('launch_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
