# Generated by Django 4.0.4 on 2022-07-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_followers_rename_contact_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='followers',
            name='facebook',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='followers',
            name='instagram',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='followers',
            name='twitter',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='followers',
            name='youtube',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='wncards',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
