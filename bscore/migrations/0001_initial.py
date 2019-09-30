# Generated by Django 2.2.5 on 2019-09-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DifferenceSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.IntegerField()),
                ('number', models.IntegerField()),
                ('occurrence', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PythagoreanTripletSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_a', models.IntegerField()),
                ('number_b', models.IntegerField()),
                ('number_c', models.IntegerField()),
                ('solution', models.IntegerField()),
                ('is_triplet', models.BooleanField()),
                ('occurrence', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
