# Generated by Django 3.1.7 on 2021-09-21 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reps', models.IntegerField(default=0)),
                ('perReps', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=4000)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('deloading', models.BooleanField(default=False)),
                ('RPE', models.IntegerField(default=0)),
                ('RIR', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'workout_list',
            },
        ),
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankbook.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankbook.workout'),
        ),
        migrations.CreateModel(
            name='ExercisedBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_part', models.CharField(max_length=30)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankbook.workout')),
            ],
            options={
                'db_table': 'exercised_part',
            },
        ),
    ]