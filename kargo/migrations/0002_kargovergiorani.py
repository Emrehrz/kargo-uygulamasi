# Generated by Django 5.2 on 2025-04-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KargoVergiOrani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vergi_orani', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
