# Generated by Django 3.1.5 on 2021-06-30 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worxpro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='categories',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
