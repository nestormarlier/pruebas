from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoriasUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    CATEGORIA_CHOICES = [
        ('SUPERVISOR', 'SUPERVISOR'),
        ('MAQUINISTA', 'MAQUINISTA'),
        ('1ER AYUDANTE', '1ER AYUDANTE'),
        ('2DO AYUDANTE', '2DO AYUDANTE'),
        ('3ER AYUDANTE', '3ER AYUDANTE'),
    ]

    categoria = models.TextField(choices=CATEGORIA_CHOICES)

    def __str__(self):
        return str(self.usuario.id) + ' - ' + self.usuario.first_name + ' - ' + self.usuario.last_name + ' - ' + self.categoria

class ParteImpresion(models.Model):
    #parte_id = models.AutoField(verbose_name='Orden impresión', primary_key=True)
    maquinista = models.ForeignKey(CategoriasUsuario, verbose_name='Maquinista', on_delete=models.DO_NOTHING,
                                   related_name='maquinista', db_column='maquinista')
    supervisor = models.ForeignKey(CategoriasUsuario, verbose_name='Supervisor', on_delete=models.DO_NOTHING,
                                   related_name='supervisor', db_column='supervisor')
    ayudante1ero = models.ForeignKey(CategoriasUsuario, verbose_name='Primer ayudante', on_delete=models.DO_NOTHING,
                                     related_name='ayudante1er', db_column='ayudante1er')
    ayudante2do = models.ForeignKey(CategoriasUsuario, verbose_name='Segundo ayudante', on_delete=models.DO_NOTHING,
                                    related_name='ayudante2do', db_column='ayudante2do')
