# Generated by Django 4.2.4 on 2023-08-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_gestion', '0004_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('votos', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
