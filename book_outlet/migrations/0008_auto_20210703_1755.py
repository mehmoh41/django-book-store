# Generated by Django 3.2.4 on 2021-07-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_alter_address_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pusblished_counteries',
            field=models.ManyToManyField(related_name='countries', to='book_outlet.Country'),
        ),
    ]
