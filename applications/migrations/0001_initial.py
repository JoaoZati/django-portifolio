# Generated by Django 3.2.9 on 2021-11-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('online_app', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ImageField(upload_to='images')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('link_github', models.TextField()),
                ('link_site', models.TextField()),
                ('application_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                       to='applications.applicationtype')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]