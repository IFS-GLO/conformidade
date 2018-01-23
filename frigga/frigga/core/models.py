from django.db import models


class Fund(models.Model):
    name = models.CharField(max_length=15, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Fundo'


class Unit(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Unidade'


class Specie(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Espécie'


class Conformity(models.Model):
    document_number = models.CharField(max_length=25, verbose_name='Número do documento')
    subject = models.CharField(max_length=120, verbose_name='Assunto')
    classification_code = models.CharField(max_length=45, verbose_name='Código de classificação')
    production_date = models.DateField(verbose_name='Data de produção')
    payment_date = models.DateField(verbose_name='Data de pagamento')
    box = models.IntegerField(verbose_name='Caixa')
    note = models.TextField(verbose_name='Observação')

    fund = models.ForeignKey(Fund, null=True, verbose_name=Fund._meta.verbose_name, on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit, null=True, verbose_name=Unit._meta.verbose_name, on_delete=models.SET_NULL)
