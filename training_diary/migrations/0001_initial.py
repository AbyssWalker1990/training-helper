# Generated by Django 4.1.2 on 2022-10-15 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_name', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=800, null=True)),
                ('date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('reps', models.IntegerField()),
                ('weight', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_diary.exercise')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_diary.training'),
        ),
    ]
