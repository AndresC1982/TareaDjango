# Generated by Django 2.2.6 on 2019-12-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='nino',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='nino',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nino',
            name='nombre',
        ),
        migrations.AddField(
            model_name='nino',
            name='person_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Person'),
            preserve_default=False,
        ),
    ]
