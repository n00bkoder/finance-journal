# Generated by Django 3.2.4 on 2021-07-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Dinning and Drinks', 'Dinning and Drinks'), ('Uncategorized', 'Uncategorized')], default='Uncategorized', max_length=250),
        ),
    ]
