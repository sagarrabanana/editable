# Generated by Django 5.0.7 on 2024-08-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parrafos', '0003_alter_parrafo_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='parrafo',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
