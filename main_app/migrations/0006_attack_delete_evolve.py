# Generated by Django 4.1.3 on 2023-01-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_evolve_delete_attack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelLearned', models.IntegerField()),
                ('move', models.CharField(choices=[('T', 'Tackle'), ('S', 'Scratch'), ('B', 'Bite')], default='T', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Evolve',
        ),
    ]
