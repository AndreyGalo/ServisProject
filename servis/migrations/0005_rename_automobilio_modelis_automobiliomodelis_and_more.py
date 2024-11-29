# Generated by Django 5.1.3 on 2024-11-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servis', '0004_alter_paslauga_pavadinimas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Automobilio_modelis',
            new_name='AutomobilioModelis',
        ),
        migrations.AlterModelOptions(
            name='automobiliomodelis',
            options={'verbose_name': 'Automobilio modelis', 'verbose_name_plural': 'Automobiliu modeliai'},
        ),
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'verbose_name': 'Užsakymas', 'verbose_name_plural': 'Užsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymo_eilute',
            options={'verbose_name': 'Užsakymų suvestinė', 'verbose_name_plural': 'Užsakymų suvestinė'},
        ),
        migrations.RenameField(
            model_name='automobilis',
            old_name='Automobilio_modelis',
            new_name='AutomobilioModelis',
        ),
        migrations.AlterField(
            model_name='paslauga',
            name='Pavadinimas',
            field=models.TextField(help_text='Trumpas paslaugos aprašymas', max_length=200, verbose_name='Aprašymas'),
        ),
        migrations.AlterField(
            model_name='uzsakymo_eilute',
            name='Kiekis',
            field=models.IntegerField(verbose_name='Paslaugu kiekis'),
        ),
    ]