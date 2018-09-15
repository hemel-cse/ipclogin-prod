# Generated by Django 2.1.1 on 2018-09-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo_id',
            field=models.ImageField(blank=True, null=True, upload_to='photo_ids/%Y-%m-%d/', verbose_name='Profile picture'),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture'),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_type',
            field=models.CharField(choices=[('CMR', 'Consumer'), ('MCT', 'Marchent'), ('ORG', 'Organization')], default='CMR', max_length=3, verbose_name='Profile Type'),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ZIP / Postal code'),
        ),
    ]