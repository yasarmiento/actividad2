# Generated by Django 4.0.4 on 2022-05-28 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculoventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=30)),
                ('valortotal', models.CharField(max_length=30)),
                ('tipopago', models.CharField(max_length=30)),
                ('usuarioid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
                ('vehiculo', models.ManyToManyField(through='usuario.Vehiculoventas', to='vehiculo.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='vehiculoventas',
            name='ventasid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.ventas'),
        ),
    ]