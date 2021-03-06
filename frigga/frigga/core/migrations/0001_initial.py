# Generated by Django 2.0.1 on 2018-01-11 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conformity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.CharField(max_length=25, verbose_name='Número do documento')),
                ('subject', models.CharField(max_length=120, verbose_name='Assunto')),
                ('classification_code', models.CharField(max_length=45, verbose_name='Código de classificação')),
                ('production_date', models.DateField(verbose_name='Data de produção')),
                ('payment_date', models.DateField(verbose_name='Data de pagamento')),
                ('box', models.IntegerField(verbose_name='Caixa')),
                ('note', models.TextField(verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Fundo',
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Espécie',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Unidade',
            },
        ),
        migrations.AddField(
            model_name='conformity',
            name='fund',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Fund', verbose_name='Fundo'),
        ),
        migrations.AddField(
            model_name='conformity',
            name='unit',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Unit', verbose_name='Unidade'),
        ),
    ]
