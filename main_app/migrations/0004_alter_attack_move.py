# Generated by Django 4.1.3 on 2023-01-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_newmove_attack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='move',
            field=models.CharField(choices=[('T', 'Tackle'), ('S', 'Scratch'), ('B', 'Bite')], default='T', max_length=100),
        ),
    ]
