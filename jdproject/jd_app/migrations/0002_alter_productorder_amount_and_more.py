# Generated by Django 4.2 on 2023-04-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jd_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(db_column='amount', default=1),
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='amount',
            new_name='_amount',
        ),
    ]
