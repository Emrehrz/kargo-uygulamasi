# Generated by Django 5.2 on 2025-04-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kisiler', '0004_rename_kisi_tipi_kisi_kisi_turu'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuzelTuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=100)),
            ],
        ),
    ]
