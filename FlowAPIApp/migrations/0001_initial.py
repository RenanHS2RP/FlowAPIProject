# Generated by Django 4.2.7 on 2023-11-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo_operacao', models.DateTimeField(auto_now_add=True)),
                ('litros_totais', models.FloatField()),
                ('litros_por_minuto', models.FloatField()),
            ],
        ),
    ]