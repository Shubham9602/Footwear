# Generated by Django 4.2.6 on 2023-11-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footapp', '0009_order_amt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]