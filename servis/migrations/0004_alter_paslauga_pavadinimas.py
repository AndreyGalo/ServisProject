# Generated by Django 5.1.3 on 2024-11-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servis', '0003_alter_automobilio_modelis_marke_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paslauga',
            name='Pavadinimas',
            field=models.TextField(help_text='Trumpas paslaugos aprašymas', max_length=500, verbose_name='Aprašymas'),
        ),
    ]