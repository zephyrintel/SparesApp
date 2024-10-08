# Generated by Django 4.2 on 2024-08-23 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Level1Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=255)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kits.kit')),
            ],
        ),
        migrations.CreateModel(
            name='Level2Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=255)),
                ('parent_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kits.level1component')),
            ],
        ),
    ]
