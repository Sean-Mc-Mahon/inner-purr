# Generated by Django 3.1.7 on 2021-05-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0016_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
