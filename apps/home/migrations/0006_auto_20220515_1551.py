# Generated by Django 3.2.11 on 2022-05-15 19:51

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_patron_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='datetime_finished',
            field=models.DateTimeField(blank=sqlalchemy.sql.expression.true, null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='patron',
            name='datetime_started',
            field=models.DateTimeField(blank=sqlalchemy.sql.expression.true, null=sqlalchemy.sql.expression.true),
        ),
        migrations.AlterField(
            model_name='patron',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
