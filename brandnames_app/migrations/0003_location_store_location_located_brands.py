# Generated by Django 4.0.1 on 2022-01-06 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brandnames_app', '0002_rename_book_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brandnames_app.brand')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brandnames_app.location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='located_brands',
            field=models.ManyToManyField(through='brandnames_app.Store', to='brandnames_app.Brand'),
        ),
    ]