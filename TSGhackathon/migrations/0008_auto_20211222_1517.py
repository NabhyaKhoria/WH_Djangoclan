# Generated by Django 2.2.9 on 2021-12-22 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TSGhackathon', '0007_auto_20211222_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='achivement',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TSGhackathon.Profile'),
        ),
    ]
