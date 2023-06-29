# Generated by Django 4.2.1 on 2023-05-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_feedbacktable_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
