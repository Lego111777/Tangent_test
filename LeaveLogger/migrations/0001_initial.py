# Generated by Django 2.2.7 on 2019-11-27 21:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_number', models.CharField(
                    max_length=10, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            managers=[
                ('employee', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('days_of_leave', models.IntegerField()),
                ('status', models.CharField(choices=[
                 ('new', 'New'), ('app', 'Approved'), ('decl', 'Declined')], default='new', max_length=10)),
                ('employee_pk', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='LeaveLogger.Employee')),
            ],
            managers=[
                ('leave', django.db.models.manager.Manager()),
            ],
        ),
    ]
