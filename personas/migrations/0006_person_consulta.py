# Generated by Django 2.2.6 on 2019-12-07 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_consulta_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.Consulta'),
        ),
    ]