# Generated by Django 4.0.6 on 2022-08-04 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente_financeiro', models.CharField(max_length=100)),
                ('operacaoDireta', models.BooleanField()),
                ('inovacao', models.BooleanField()),
                ('subsetorApoiado', models.CharField(max_length=100)),
                ('reembolsavel', models.BooleanField()),
                ('uf', models.CharField(max_length=100)),
                ('produtoBndes', models.CharField(max_length=100)),
                ('dataContratacao', models.CharField(max_length=100)),
                ('liquidada', models.BooleanField()),
                ('setorApoiado', models.CharField(max_length=100)),
                ('custoFinanceiro', models.CharField(max_length=100)),
                ('cnae', models.CharField(max_length=100)),
                ('formaApoio', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('valorDesembolsado', models.FloatField(null=True)),
                ('porteCliente', models.CharField(max_length=100, null=True)),
                ('municipio', models.CharField(max_length=100, null=True)),
                ('prazoAmortizacao', models.IntegerField(default=0)),
                ('cnpjAberto', models.CharField(max_length=100, null=True)),
                ('instrumentoBndes', models.CharField(max_length=100, null=True)),
                ('naturezaCliente', models.CharField(max_length=100, null=True)),
                ('prazoCarencia', models.CharField(max_length=100, null=True)),
                ('tipoOperacao', models.CharField(max_length=100, null=True)),
                ('cliente', models.CharField(max_length=100, null=True)),
                ('tipoDocumento', models.CharField(max_length=100, null=True)),
                ('fonteRecursos', models.CharField(max_length=100, null=True)),
                ('cnpjAgenteFinanceiro', models.CharField(max_length=100, null=True)),
                ('taxaJuros', models.SmallIntegerField(default=0)),
                ('areaOperacional', models.CharField(max_length=200, null=True)),
                ('codigoMunicipio', models.CharField(max_length=100, null=True)),
                ('ramoAtividade', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.operacoes')),
            ],
        ),
    ]
