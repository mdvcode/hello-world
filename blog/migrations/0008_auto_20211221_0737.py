# Generated by Django 3.2.9 on 2021-12-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211221_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
