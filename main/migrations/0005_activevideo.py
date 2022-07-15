# Generated by Django 4.0.4 on 2022-07-15 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_alter_followers_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categories')),
            ],
        ),
    ]
