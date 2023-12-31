# Generated by Django 4.2.4 on 2023-08-15 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jsbackend', '0003_alter_fornecedor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='móveis', to='jsbackend.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='móveis', to='jsbackend.fornecedor')),
            ],
        ),
    ]
