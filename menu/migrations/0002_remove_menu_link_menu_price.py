# Generated by Django 4.1.5 on 2023-02-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='link',
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.CharField(max_length=200, null=True, verbose_name='Precio'),
        ),
    ]