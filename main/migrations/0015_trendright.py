# Generated by Django 3.2.12 on 2022-07-18 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_trendbottom_trendtop'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categories')),
            ],
        ),
    ]