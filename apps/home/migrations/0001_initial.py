# Generated by Django 3.2.11 on 2022-05-14 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('photo_count', models.IntegerField(default=0)),
                ('minor_passport_count', models.IntegerField(default=0)),
                ('adult_passport_count', models.IntegerField(default=0)),
                ('expidited_passport_count', models.IntegerField(default=0)),
                ('datetime_submitted', models.DateTimeField(auto_now_add=True, null=sqlalchemy.sql.expression.true)),
                ('datetime_started', models.DateTimeField(null=sqlalchemy.sql.expression.true)),
                ('datetime_finished', models.DateTimeField(null=sqlalchemy.sql.expression.true)),
                ('status', models.TextField(choices=[('waiting', 'Waiting'), ('in_progress', 'In Progress'), ('executed', 'Executed'), ('cancelled', 'Cancelled'), ('coming_back', 'Coming Back')])),
                ('active', models.BooleanField(default=sqlalchemy.sql.expression.true)),
                ('order', models.IntegerField(default=0)),
                ('agent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='patron', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
