# Generated by Django 4.0.4 on 2022-05-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('ingrediente_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nome_en', models.CharField(max_length=255)),
                ('nome_alt', models.CharField(max_length=255)),
                ('nome_br', models.CharField(max_length=255)),
                ('origem', models.TextField()),
                ('funcao_principal', models.TextField()),
                ('referencia', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
