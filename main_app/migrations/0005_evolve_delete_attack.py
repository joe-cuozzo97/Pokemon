# Generated by Django 4.1.3 on 2023-01-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_attack_move'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newName', models.CharField(max_length=100)),
                ('levelEvolved', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Attack',
        ),
    ]