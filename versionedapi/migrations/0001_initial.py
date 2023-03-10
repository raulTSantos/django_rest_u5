# Generated by Django 4.1.3 on 2022-12-29 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(default='', null=True, upload_to='images/', verbose_name='Logo tipo')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('paymentDate', models.DateField(auto_now_add=True)),
                ('expirationDate', models.DateField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versionedapi.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment_user',
            },
        ),
        migrations.CreateModel(
            name='Expired_payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.DecimalField(decimal_places=2, default=40.0, max_digits=9)),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='versionedapi.payment_user')),
            ],
            options={
                'db_table': 'expired_payments',
            },
        ),
    ]
