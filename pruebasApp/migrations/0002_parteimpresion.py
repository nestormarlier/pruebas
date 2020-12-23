# Generated by Django 2.2 on 2020-12-19 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParteImpresion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ayudante1ero', models.ForeignKey(db_column='ayudante1er', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante1er', to='pruebasApp.CategoriasUsuario', verbose_name='Primer ayudante')),
                ('ayudante2do', models.ForeignKey(db_column='ayudante2do', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ayudante2do', to='pruebasApp.CategoriasUsuario', verbose_name='Segundo ayudante')),
                ('maquinista', models.ForeignKey(db_column='maquinista', on_delete=django.db.models.deletion.DO_NOTHING, related_name='maquinista', to='pruebasApp.CategoriasUsuario', verbose_name='Maquinista')),
                ('supervisor', models.ForeignKey(db_column='supervisor', on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor', to='pruebasApp.CategoriasUsuario', verbose_name='Supervisor')),
            ],
        ),
    ]