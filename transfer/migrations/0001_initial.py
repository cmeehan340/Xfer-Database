# Generated by Django 3.0.4 on 2020-04-12 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MajorRequirment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100, unique=True)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Major')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_no', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('sem_year_taken', models.CharField(max_length=8)),
                ('expiration_date', models.DateField()),
                ('approved_status', models.CharField(max_length=1)),
                ('comment', models.CharField(max_length=150)),
                ('approver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Approver')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.School')),
            ],
        ),
    ]