# Generated by Django 3.2.12 on 2022-07-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20220724_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendtop',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
