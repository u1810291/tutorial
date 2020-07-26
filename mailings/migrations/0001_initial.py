# Generated by Django 3.0.8 on 2020-07-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonMailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Email подаписчика')),
            ],
            options={
                'db_table': 'common_mailing_list',
            },
        ),
        migrations.CreateModel(
            name='CaseMailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, verbose_name='Email подаписчика')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.Case', verbose_name='Дуло')),
            ],
            options={
                'db_table': 'case_mailing_list',
            },
        ),
    ]
