# Generated by Django 4.0.3 on 2024-05-26 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='locality',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='customer',
            name='rollNumber',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Me', 'Medical'), ('Mec', 'Mechanical'), ('Eng', 'Engineering')], max_length=50),
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
    ]