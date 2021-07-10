# Generated by Django 3.1.7 on 2021-07-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Id', models.IntegerField()),
                ('Student_Name', models.CharField(max_length=30)),
                ('Student_DOB', models.DateField()),
                ('Student_DOJ', models.DateField()),
            ],
            options={
                'db_table': 'studentcrud',
            },
        ),
    ]