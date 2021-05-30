# Generated by Django 3.2.2 on 2021-05-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_approved_by_line_manager',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_approved_by_zonal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_modified_by_internal_control',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='internal_control_comment',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='line_manager_comment',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='requester_comment',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='zonal_comment',
            field=models.CharField(blank=True, max_length=200000, null=True),
        ),
    ]
