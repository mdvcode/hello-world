# Generated by Django 3.2.9 on 2022-07-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0017_auto_20220608_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmetamask',
            name='private_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
