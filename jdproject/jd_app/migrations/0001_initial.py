# Generated by Django 4.2 on 2023-04-21 20:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('pickup', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('composition', models.TextField(default='Состав не указан')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='jd_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('DI', 'Директор'), ('AD', 'Администратор'), ('CO', 'Повар'), ('CA', 'Кассир'), ('CL', 'Уборщик'), ('OW', 'Owner'), ('MS', 'Master')], default='CA', max_length=2)),
                ('labor_contract', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_amount', models.IntegerField(db_column='amount', default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jd_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jd_app.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='jd_app.ProductOrder', to='jd_app.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jd_app.staff'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingAuthor', models.SmallIntegerField(default=0)),
                ('full_name', models.CharField(max_length=128)),
                ('age', models.IntegerField(blank=True)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
